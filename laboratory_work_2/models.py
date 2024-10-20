"""Models"""

# pylint: disable=R0913, E0401

import math as mt

import numpy as np

from characteristics import Characteristics as Characts
from rendering import Rendering as Render


class Model(Characts, Render):
    """Models"""

    def __init__(self) -> None:
        super().__init__(self)

    def ideal(self, data_size, coef) -> np.ndarray:
        """
        Модель ідеального тренду

        :param data_size: Довжина даних
        :param coef: Коефіцієнт для квадратичної моделі
        :param sqrt: Піднесення до квадрату

        :return: Массив даних, що відповідає ідеальному тренду
        """

        return coef * np.arange(data_size) ** 2

    def permanent(self, data_size, val) -> np.ndarray:
        """
        Модель постійного тренду

        :param data_size: Довжина даних
        :param val: Значення, що додається

        :return: Массив даних, що відповідає постійному тренду
        """

        return np.full(data_size, val)

    def normal(self, data, expan) -> np.ndarray:  # Адитивна суміш
        """
        Модель нормального тренду

        :param data: Математичне сподівання (середнє значення)
        :param expan: Массив ідеальних значень для моделі

        :return: Массив згенерованих значень, що відповідають нормальному розподілу
        """

        return data + expan

    # uniform,
    def abnormal(
        self, data, abnorm_size, coef, coef_prefer, mean=0, mean_sqrt=0
    ) -> np.ndarray:
        # def abnormal(self, data_size, data, coef, mean=0, mean_sqrt=0) -> np.ndarray:
        """
        Модель аномального тренду

        :param uniform: Массив рівномірно розподілених індексів
        :param ideal: Массив ідеальних значень для моделі
        :param normal: Массив нормальних значень
        :param data_size: Кількість даних для генерації
        :param coef: Коефіцієнт для моделі
        :param deviat: Стандартне відхилення для нормального закону розподілу
        :param mean: Коефіцієнт для нормального закону розподілу

        :return: Массив даних із доданими аномальними похибками
        """

        # random_indices = np.random.choice(data_size, data_size, replace=False)

        ideal_model = self.ideal(len(data), coef)
        normal_model = self.normal(ideal_model, data)

        model_data = normal_model
        normal_data = np.random.normal(
            mean, (coef_prefer * mean_sqrt), abnorm_size
        )  # аномальна випадкова похибка з нормальним законом

        for i in range(abnorm_size):
            k = int(data[i])
            # k = random_indices[i]
            model_data[k] = (
                ideal_model[k] + normal_data[i]
            )  # аномальні вимірів з рівномірно розподіленими номерами

        return model_data

    def mnk(self, data: np.ndarray) -> np.ndarray:
        """
        МНК згладжування для визначення статистичних характеристик.

        Виконує метод найменших квадратів (МНК) для знаходження тренду вхідних даних.

        :param data: Вхідні дані у вигляді одномірного масиву.

        :return: Масив значень тренду, отриманих за допомогою МНК.
        """

        data_size = len(data)
        yin = np.zeros((data_size, 1))  # Матриця вхідних даних
        f = np.ones((data_size, 3))  # Матриця функцій для МНК

        # Формування структури вхідних матриць МНК
        for i in range(data_size):
            yin[i, 0] = float(data[i])  # Матриця вхідних даних
            f[i, 1] = float(i)
            f[i, 2] = float(i * i)

        ft = f.T  # Транспонована матриця
        fft = ft.dot(f)  # Добуток матриць
        ffti = np.linalg.inv(fft)  # Обернена матриця
        fftift = ffti.dot(ft)  # Добуток оберненої матриці і транспонованої
        c = fftift.dot(yin)  # Коефіцієнти тренду
        trend = f.dot(c)  # Розрахунок тренду

        return trend

    # def _mnk_av_detect(self, data):
    #     """МНК детекція та очищення АВ"""

    #     data_size = len(data)
    #     yin = np.zeros((data_size, 1))
    #     F = np.ones((data_size, 3))
    #     for i in range(data_size):  # формування структури вхідних матриць МНК
    #         yin[i, 0] = float(data[i])  # формування матриці вхідних даних
    #         F[i, 1] = float(i)
    #         F[i, 2] = float(i * i)
    #     FT = F.T
    #     FFT = FT.dot(F)
    #     FFTI = np.linalg.inv(FFT)
    #     FFTIFT = FFTI.dot(FT)
    #     C = FFTIFT.dot(yin)

    #     return C[1, 0]

    def mnk_extrapol(self, data, coef) -> np.ndarray:
        """статистичні характеристики екстраполяції"""

        data_size = len(data)
        extrapol = np.zeros((data_size + coef, 1))
        yin = np.zeros((data_size, 1))
        f = np.ones((data_size, 3))

        for i in range(data_size):  # формування структури вхідних матриць МНК
            yin[i, 0] = float(data[i])  # формування матриці вхідних даних
            f[i, 1] = float(i)
            f[i, 2] = float(i * i)

        ft = f.T
        fft = ft.dot(f)
        ffti = np.linalg.inv(fft)
        fftift = ffti.dot(ft)
        c = fftift.dot(yin)

        for i in range(data_size + coef):
            extrapol[i, 0] = (
                c[0, 0] + c[1, 0] * i + (c[2, 0] * i * i)
            )  # проліноміальна крива МНК - прогнозування

        return extrapol

    def sliding_wind(self, data, wind) -> np.ndarray:
        """sliding_wind"""

        # ---- параметри циклів ----
        data_size = len(data)
        j_wind = mt.ceil(data_size - wind) + 1
        data_wind = np.zeros((wind))
        midi = np.zeros((data_size))

        # ---- ковзне вікно ---------
        for j in range(j_wind):
            for i in range(wind):
                l = j + i
                data_wind[i] = data[l]
            # - Стат хар ковзного вікна --
            midi[l] = np.median(data_wind)
        # ---- очищена вибірка  -----
        data_midi = np.zeros((data_size))

        for j in range(data_size):
            data_midi[j] = midi[j]

        for j in range(wind):
            data_midi[j] = data[j]

        return data_midi

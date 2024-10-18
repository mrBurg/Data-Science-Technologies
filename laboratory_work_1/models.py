"""Models"""

# pylint: disable=R0913, E0401

import numpy as np

from characteristics import Characteristics as Characts
from rendering import Rendering as Render


class Model(Characts, Render):
    """Models"""

    def __init__(self) -> None:
        super().__init__(self)

    def permanent(self, data_size, val) -> np.ndarray:  # Тренд
        """
        Модель постійного тренду

        :param data_size: Довжина даних (кількість точок)
        :param val: Значення, що додається
        :return: Массив даних, що відповідає постійному тренду
        """

        return np.full(data_size, val)

    def normal(self, data, expan) -> np.ndarray:  # Адитивна суміш
        """
        Генерація значень за нормальним законом розподілу

        :param data: Математичне сподівання (середнє значення)
        :param expan: Массив ідеальних значень для моделі
        :return: Массив згенерованих значень, що відповідають нормальному розподілу
        """

        return data + expan

    def mnk(self, data: np.ndarray) -> np.ndarray:
        """
        МНК згладжування для визначення статистичних характеристик.

        Виконує метод найменших квадратів (МНК) для знаходження тренду вхідних даних.

        :param data: Вхідні дані у вигляді одномірного масиву.
        :return: Масив значень тренду, отриманих за допомогою МНК.
        """
        data_len = len(data)
        yin = np.zeros((data_len, 1))  # Матриця вхідних даних
        f = np.ones((data_len, 3))  # Матриця функцій для МНК

        # Формування структури вхідних матриць МНК
        for i in range(data_len):
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

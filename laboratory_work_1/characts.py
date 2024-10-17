"""Characteristics"""

from dataclasses import dataclass
import math as mt

import numpy as np


@dataclass
class Characts:
    """Get characteristics"""

    def all(self, data):
        """
        Виводить всі статистичні характеристики розподілу.

        :param data: Масив чисел, для якого потрібно розрахувати статистичні характеристики.

        Виводить:
            - Номери елементів масиву `data`
            - Математичне сподівання (середнє значення)
            - Дисперсію (варіацію)
            - Середньо-квадратичне відхилення
        """

        average_val = np.mean(data)
        dispersion = np.var(data)
        mean_square = np.sqrt(dispersion)

        print("-" * 20)
        print("Номери: ", data)
        print("\n<<< Статистичні характеристики розподілу >>>")
        print("Матиматичне сподівання: ", average_val)
        print("Дисперсія: ", dispersion)
        print("Середньо-квадратичне відхилення: ", mean_square)
        print("-" * 20)

    def __mnk_stat_characts(self, data: np.ndarray) -> np.ndarray:
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

    def stat_in(self, data, text):
        """Статистичні характеристики вибірки з урахуванням тренду"""

        trend = self.__mnk_stat_characts(data)
        trend_len = len(trend)
        result = np.subtract(data[:trend_len], trend[:trend_len, 0])
        mean = np.mean(result)
        dispersion = np.var(result)
        mean_square = mt.sqrt(dispersion)

        print("-" * 20)
        print("-" * 10, text, "-" * 10)
        print("Кількість елементів вбірки: ", trend_len)
        print("Матиматичне сподівання: ", mean)
        print("Дисперсія: ", dispersion)
        print("СКВ: ", mean_square)
        print("-" * 20)

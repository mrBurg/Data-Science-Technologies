"""Characteristics"""

# pylint: disable=R0913

from typing import TYPE_CHECKING
import math as mt
from abc import ABC


import numpy as np

if TYPE_CHECKING:
    from models import Model


class Characteristics(ABC):
    """Get characteristics"""

    def __init__(self, model: "Model") -> None:
        self.model = model

    def _print_data(self, title, data, mean, dispersion, mean_sqrt) -> None:
        """
        Виводить всі статистичні характеристики розподілу.

        :param title: Назва блоку.
        :param data: Масив чисел, для якого потрібно розрахувати статистичні характеристики.
        :param mean: Математичне сподівання.
        :param dispersion: Дисперсія.
        :param mean_sqrt: Середньо-квадратичне відхилення (СКВ).

        Виводить:
            - Кількість елементів вбірки
            - Математичне сподівання (середнє значення)
            - Дисперсію (варіацію)
            - Середньо-квадратичне відхилення
        """

        text = "-" * 10 + title + "-" * 10
        divider = "-" * len(text)

        print(divider)
        print(text)
        print("Кількість елементів вбірки: ", len(data))
        print("Математичне сподівання: ", mean)
        print("Дисперсія: ", dispersion)
        print("Середньо-квадратичне відхилення (СКВ): ", mean_sqrt)
        print(divider)

    def stat_characts(self, data, title) -> None:
        """
        Розраховує всі статистичні характеристики розподілу.

        :param data: Масив чисел, для якого потрібно розрахувати статистичні характеристики.
        :param title: Назва блоку.
        """

        mean = np.mean(data)
        dispersion = np.var(data)
        mean_sqrt = np.sqrt(dispersion)

        self._print_data(title, data, mean, dispersion, mean_sqrt)

    def stat_characts_in(self, data, title) -> None:
        """Статистичні характеристики вибірки з урахуванням тренду"""

        trend = self.model.mnk(data)
        trend_len = len(trend)
        data = np.subtract(data[:trend_len], trend[:trend_len, 0])

        mean = np.mean(data)
        dispersion = np.var(data)
        mean_sqrt = mt.sqrt(dispersion)

        self._print_data(title, trend, mean, dispersion, mean_sqrt)

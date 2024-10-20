"""Characteristics"""

# pylint: disable=R0913, E0401

from typing import TYPE_CHECKING
import math as mt
from abc import ABC  # abstractmethod


import numpy as np

if TYPE_CHECKING:
    from models import Model


class Characteristics(ABC):
    """Get characteristics"""

    def __init__(self, model: "Model") -> None:
        self.model = model

    # @abstractmethod метод помічений як @abstractmethod необхідно реалізовувати у класі нащадка
    def _print_data(
        self,
        title,
        data,
        dispersion,
        mean_sqrt,
        mean_sqrt_extrapol=None,
        delta=None,
    ) -> None:
        """
        Виводить всі статистичні характеристики розподілу.

        :param title: Назва блоку.
        :param data: Масив чисел, для якого потрібно розрахувати статистичні характеристики.
        :param mean: Математичне сподівання.
        :param dispersion: Дисперсія.
        :param mean_sqrt: Середньо-квадратичне відхилення (СКВ).
        :param delta: Динамічна похибка моделі.
        :param mean_sqrt: Прогнозоване середньо-квадратичне відхилення (ПСКВ).

        Виводить:
            - Кількість елементів вбірки
            - Математичне сподівання (середнє значення)
            - Дисперсію (варіацію)
            - Середньо-квадратичне відхилення
        """

        mean = np.mean(data)

        text = "-" * 10 + title + "-" * 10
        divider = "-" * len(text)

        print(divider)
        print(text)
        print("Кількість елементів вбірки: ", len(data))
        print("Математичне сподівання: ", mean)
        print("Дисперсія: ", dispersion)
        print("Середньо-квадратичне відхилення (СКВ): ", mean_sqrt)

        if np.any(delta):
            print("Динамічна похибка моделі: ", delta)

        if np.any(mean_sqrt_extrapol):
            print(
                "Прогнозоване середньо-квадратичне відхилення (ПСКВ): ",
                mean_sqrt_extrapol,
            )

        print(divider)

    def stat_characts(self, data, title) -> None:
        """
        Розраховує всі статистичні характеристики розподілу.

        :param data: Масив чисел, для якого потрібно розрахувати статистичні характеристики.
        :param title: Назва блоку.
        """

        dispersion = np.var(data)
        mean_sqrt = np.sqrt(dispersion)

        self._print_data(title, data, dispersion, mean_sqrt)

    def stat_characts_in(self, data, title) -> None:
        """Статистичні характеристики вибірки з урахуванням тренду"""

        trend = self.model.mnk(data)
        trend_len = len(trend)
        data = np.subtract(data[:trend_len], trend[:trend_len, 0])

        dispersion = np.var(data)
        mean_sqrt = mt.sqrt(dispersion)

        self._print_data(title, trend, dispersion, mean_sqrt)

    def stat_characts_out(self, data, data_sw, title) -> None:
        """Статистичні характеристики вибірки з урахуванням тренду"""

        trend = self.model.mnk(data)
        trend_len = len(trend)
        data_subtract = np.subtract(data_sw[:trend_len], trend[:trend_len])

        dispersion = np.var(data_subtract)
        mean_sqrt = mt.sqrt(dispersion)

        delta = 0

        for i in range(trend_len):
            delta = delta + abs(data[i] - trend[i])

        delta = delta / (trend_len + 1)

        self._print_data(title, trend, dispersion, mean_sqrt, delta=delta)

    def stat_characts_extrapol(self, data, coef, title) -> None:
        """Статистичні характеристики екстрополярної вибірки з урахуванням тренду"""

        trend = self.model.mnk(data)
        trend_len = len(trend)
        new_data = np.zeros((trend_len))

        for i in range(trend_len):
            new_data[i] = data[i, 0] - trend[i, 0]

        dispersion = np.var(new_data)
        mean_sqrt = mt.sqrt(dispersion)
        mean_sqrt_extrapol = (
            mean_sqrt * coef
        )  #  довірчий інтервал прогнозованих значень за СКВ

        self._print_data(
            title,
            trend,
            dispersion,
            mean_sqrt,
            mean_sqrt_extrapol=mean_sqrt_extrapol,
        )

    def qual_assess(self, data, model, title):  # determination
        """Коефіцієнт детермінації - оцінювання якості моделі"""
        # статистичні характеристики вибірки з урахуванням тренду

        data_size = len(model)
        numerator = 0
        denominator_1 = 0

        for i in range(data_size):
            numerator = numerator + (data[i] - model[i, 0]) ** 2
            denominator_1 = denominator_1 + data[i]

        denominator_2 = 0

        for i in range(data_size):
            denominator_2 = denominator_2 + (data[i] - (denominator_1 / data_size)) ** 2

        r2_score_our = 1 - (numerator / denominator_2)

        text = "-" * 10 + title + "-" * 10
        divider = "-" * len(text)

        print(divider)
        print(text)
        print("Кількість елементів вбірки: ", data_size)
        print(
            "Коефіцієнт детермінації (ймовірність апроксимації)",
            r2_score_our,
        )
        print(divider)

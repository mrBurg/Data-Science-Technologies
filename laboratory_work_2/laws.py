"""Characteristics"""

from dataclasses import dataclass

import numpy as np

from rendering import Render


@dataclass
class Laws(Render):
    """Клас Laws для генерації даних з різними законами розподілу."""

    def even(self, data_len: int, max_val: int = 100) -> np.ndarray:
        """
        Генерує дані за рівномірним законом розподілу.

        :param data_len: Кількість точок даних для генерації.
        :param max_val: Максимальне значення для рівномірного розподілу.
        :return: Масив з рівномірно розподіленими даними.
        """

        return np.ceil(np.random.randint(1, max_val, data_len)).astype(int)

    def normal(
        self, data_len: int, mean: float = 0, deviation: float = 100
    ) -> np.ndarray:
        """
        Генерує дані за нормальним (Гаусівським) законом розподілу.

        :param data_len: Кількість точок даних для генерації.
        :param mean: Середнє значення нормального розподілу.
        :param deviation: Стандартне відхилення нормального розподілу.
        :return: Масив з нормально розподіленими даними.
        """

        return np.random.normal(mean, deviation, data_len)

    def exponential(self, data_len: int, lam: float = 1.5) -> np.ndarray:
        """
        Генерує дані за експоненційним законом розподілу.

        :param data_len: Кількість точок даних для генерації.
        :param lam: Параметр швидкості (лямбда) для експоненційного розподілу.
        :return: Масив з експоненційно розподіленими даними.
        """

        return np.random.exponential(1 / lam, data_len)

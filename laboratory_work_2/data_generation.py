"""Characteristics"""

# pylint: disable=E0401

from dataclasses import dataclass

import numpy as np


@dataclass
class DataGeneration:
    """Клас DataGeneration для генерації даних з різними законами розподілу."""

    def uniform(self, data_size: int, max_val, min_val=0) -> np.ndarray:
        """
        Генерує випадкові дані за рівномірним законом розподілу.

        :param data_size: Кількість точок даних для генерації.
        :param max_val: Максимальне значення для рівномірного розподілу.
        :param min_val: Мінімальне значення для рівномірного розподілу. За замовчуванням – 0

        :return: Масив з рівномірно розподіленими даними.
        """

        return np.random.uniform(min_val, max_val, data_size)

    def normal(self, data_size: int, deviat, mean: float = 0) -> np.ndarray:
        """
        Генерує випадкові дані за нормальним (Гаусівським) законом розподілу.

        :param data_size: Кількість точок даних для генерації.
        :param deviat: Стандартне відхилення нормального розподілу.
        :param mean: Середнє значення нормального розподілу.

        :return: Масив з нормально розподіленими даними.
        """

        return np.random.normal(mean, deviat, data_size)

    def exponential(self, data_size: int, alfa) -> np.ndarray:
        """
        Генерує випадкові дані за експоненційним законом розподілу.

        :param data_size: Кількість точок даних для генерації.
        :param alfa: Параметр швидкості (лямбда) для експоненційного розподілу.

        :return: Масив з експоненційно розподіленими даними.
        """

        return np.random.exponential(alfa, data_size)

    def chisquare(self, data_size: int, deg_free) -> np.ndarray:
        """
        Генерує випадкові дані за хі-квадрат розподілом.

        :param deg_free: Кількість ступенів свободи.
        :param data_size: Кількість значень, що будуть згенеровані.

        :return: Масив з хі квадрат розподіленими даними.
        """

        return np.random.chisquare(deg_free, data_size)

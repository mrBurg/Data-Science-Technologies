"""Characteristics"""

# pylint: disable=E1121, E0401

from dataclasses import dataclass

import numpy as np


@dataclass
class DataGeneration:
    """Клас Laws для генерації даних з різними законами розподілу."""

    def uniform(self, data_size: int, max_val, min_val=0) -> np.ndarray:
        """
        Генерує дані за рівномірним законом розподілу.

        :param data_size: Кількість точок даних для генерації.
        :param max_val: Максимальне значення для рівномірного розподілу.
        :param min_val: Мінімальне значення для рівномірного розподілу. За замовчуванням – 0
        :return: Масив з рівномірно розподіленими даними.
        """

        return np.random.uniform(min_val, max_val, data_size)

"""Voronin"""

# pylint: disable=E0401

from dataclasses import dataclass

from matrix import Matrix


@dataclass
class Voronin(Matrix):
    """Voronin"""

    def __init__(self, integro, min_val):
        opt = 0

        for i, item in enumerate(integro):
            if min_val > item:
                min_val = item
                opt = i

        print("Інтегрована оцінка (scor):")
        print(integro)
        print("Номер_оптимального_товару:", opt)

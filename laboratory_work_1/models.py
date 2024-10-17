"""Models"""

# pylint: disable=R0913

import numpy as np


class Model:
    """Models"""

    def ideal(self, data_len, coef=0.0000005):
        """
        Модель ідеального тренду (квадратичний закон)

        :param data_len: Довжина даних (кількість точок)
        :param coef: Коефіцієнт для квадратичної моделі
        :return: Массив даних, що відповідає ідеальному тренду
        """

        return coef * np.arange(data_len) ** 2

    def norm(self, mean, ideal):
        """
        Генерація значень за нормальним законом розподілу

        :param mean: Математичне сподівання (середнє значення)
        :param ideal: Массив ідеальних значень для моделі
        :return: Массив згенерованих значень, що відповідають нормальному розподілу
        """

        return mean + ideal

    def abnormal(self, even, ideal, norm, size, coef, deviation):
        """
        Генерація аномальних даних з випадковими похибками

        :param even: Массив рівномірно розподілених індексів
        :param ideal: Массив ідеальних значень для моделі
        :param norm: Массив нормальних значень
        :param size: Кількість даних для генерації
        :param coef: Коефіцієнт для нормального закону розподілу
        :param dsig: Стандартне відхилення для нормального закону розподілу
        :return: Массив даних із доданими аномальними похибками
        """

        data = norm
        norm = np.random.normal(0, (coef * deviation), size)

        # аномальна випадкова похибка з нормальним законом
        for i in range(size):
            k = int(even[i])
            data[k] = (
                ideal[k] + norm[i]
            )  # аномальні вимірів з рівномірно розподіленими номерами

        return data

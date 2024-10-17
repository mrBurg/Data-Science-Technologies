"""Models"""

# pylint: disable=R0913

import numpy as np


class Model:
    """Models"""

    def ideal(self, data_len, coef=0.1, deg=1):
        """
        Модель ідеального тренду (квадратичний закон)

        :param data_len: Довжина даних (кількість точок)
        :param coef: Коефіцієнт для квадратичної моделі
        :param sqrt: Піднесення до квадрату
        :return: Массив даних, що відповідає ідеальному тренду
        """

        return coef * np.arange(data_len) ** deg

    def normal(self, data, expan):
        """
        Генерація значень за нормальним законом розподілу

        :param data: Математичне сподівання (середнє значення)
        :param expan: Массив ідеальних значень для моделі
        :return: Массив згенерованих значень, що відповідають нормальному розподілу
        """

        return data + expan

    def abnormal(self, even, ideal, normal, data_len, coef, dev, mean=0):
        """
        Генерація аномальних даних з випадковими похибками

        :param even: Массив рівномірно розподілених індексів
        :param ideal: Массив ідеальних значень для моделі
        :param normal: Массив нормальних значень
        :param data_len: Кількість даних для генерації
        :param coef: Коефіцієнт для моделі
        :param dev: Стандартне відхилення для нормального закону розподілу
        :param mean: Коефіцієнт для нормального закону розподілу
        :return: Массив даних із доданими аномальними похибками
        """

        data = normal
        data_normal = np.random.normal(
            mean, (coef * dev), data_len
        )  # аномальна випадкова похибка з нормальним законом

        for i in range(data_len):
            k = int(even[i])
            data[k] = (
                ideal[k] + data_normal[i]
            )  # аномальні вимірів з рівномірно розподіленими номерами

        return data

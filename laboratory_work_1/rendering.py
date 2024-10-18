"""Rendering"""

from abc import ABC

import matplotlib.pyplot as plt


class Rendering(ABC):
    """Rendering of data"""

    def hist(self, data, facecolor="#7eb253", **kwargs) -> None:
        """
        Відображає гістограму результатів за допомогою matplotlib.

        :param data: Масив або список чисел, які потрібно відобразити на гістограмі.
        :param wargs: Додаткові параметри для налаштування гістограми:
            - bins (int): Кількість бінів для гістограми.
            - facecolor (str): Колір гістограми.
            - alpha (float): Прозорість гістограми.
        """

        plt.hist(
            data,
            facecolor=facecolor,
            **kwargs,
        )
        plt.legend(loc="lower center")
        plt.show()

    def plot(self, title, *data, xlabel="X-axis", ylabel="Y-axis", **kwargs) -> None:
        """
        Візуалізує дві криві на одному графіку.

        :param data1: Перший масив даних (наприклад, початкова помилка).
        :param data2: Другий масив даних (наприклад, ймовірність).
        :param text: Назва графіка, що відображається на осі Y.

        :return: None. Функція не повертає значення, а лише відображає графік.

        Викликає:
            - plt.clf(): Очищає поточний графік перед побудовою нового.
            - plt.plot(): Функція для побудови графіка.
            - plt.xlabel(): Встановлює мітку для осі X.
            - plt.ylabel(): Встановлює мітку для осі Y.
            - plt.show(): Функція для відображення побудованого графіка.
        """

        plt.clf()  # Очищення холста

        for i in data:
            plt.plot(i, **kwargs)
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.show()

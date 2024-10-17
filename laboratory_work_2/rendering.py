"""Rendering"""

import matplotlib.pyplot as plt


class Render:
    """Render data results"""

    def hist(self, data, **wargs):
        """
        Відображає гістограму результатів за допомогою matplotlib.

        :param data: Масив або список чисел, які потрібно відобразити на гістограмі.
        :param wargs: Додаткові параметри для налаштування гістограми:
            - bins (int): Кількість бінів для гістограми.
            - facecolor (str): Колір гістограми.
            - alpha (float): Прозорість гістограми.
        """

        bins = wargs.get("bins")
        facecolor = wargs.get("facecolor")
        alpha = wargs.get("alpha")

        plt.hist(
            data,
            bins=bins or 20,
            facecolor=facecolor or "#7eb253",
            alpha=alpha or 0.5,
        )
        plt.show()

    def plot(self, data1, data2, text):
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
        plt.plot(data2)
        plt.plot(data1)
        plt.xlabel("Похибка")
        plt.ylabel("Ймовірність")
        plt.ylabel(text)
        plt.show()

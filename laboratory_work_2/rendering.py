"""Rendering"""

from abc import ABC

import matplotlib.pyplot as plt
import numpy as np


class Rendering(ABC):
    """Rendering of data"""

    def _show_naming(self, graph_type, *args, **kwargs):

        title = kwargs.pop("title", "")
        labels = kwargs.pop("labels", [])
        loc = kwargs.get("loc", "best")
        xlabel = kwargs.pop("xlabel", "X-axis")
        ylabel = kwargs.pop("ylabel", "Y-axis")

        min_val = np.inf
        max_val = -np.inf

        for i in args:
            min_val = min(min_val, np.min(i))
            max_val = max(max_val, np.max(i))

        plt.clf()  # Очищення холста

        match graph_type:
            case "hist":
                for i in args:
                    plt.hist(i, **kwargs)
            case "plot":
                for i in args:
                    plt.plot(i, **kwargs)

        plt.title(title)
        plt.legend(labels, loc=loc)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.ylim(min_val, max_val)
        plt.show()

    def hist(self, *data, **kwargs) -> None:
        """
        Відображає гістограму результатів.

        :param *data: Дані для відображення.
        :param **wargs: Додаткові параметри для налаштування гістограми.
        """

        self._show_naming("hist", *data, **kwargs)

    def plot(self, *data, **kwargs) -> None:
        """
        Візуалізує дані на графіку.

        :param *data: Дані для відображення.
        :param **wargs: Додаткові параметри для налаштування графіку.
        """

        self._show_naming("plot", *data, **kwargs)

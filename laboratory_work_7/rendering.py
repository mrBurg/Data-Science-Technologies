"""Rendering"""

from abc import ABC
from dataclasses import dataclass

import matplotlib.pyplot as plt


@dataclass
class Rendering(ABC):
    """Rendering of data"""

    @staticmethod
    def show(*data, **kwargs):
        """show"""

        title = kwargs.pop("title", None)
        labels = kwargs.pop("labels", None)
        xlabel = kwargs.pop("xlabel", None)  # "X-axis"
        ylabel = kwargs.pop("ylabel", None)  # "Y-axis"
        loc = kwargs.get("loc", "best")

        if title:
            plt.title(title)

        for i in data:
            plt.plot(i, **kwargs)

        if labels and len(labels):
            plt.legend(labels, loc=loc)

        if xlabel:
            plt.xlabel(xlabel)

        if ylabel:
            plt.ylabel(ylabel)

        plt.show()

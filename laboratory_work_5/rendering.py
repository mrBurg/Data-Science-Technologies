"""Rendering"""

from abc import ABC
from dataclasses import dataclass

import matplotlib.pyplot as plt


@dataclass
class Rendering(ABC):
    """Rendering of data"""

    def show(self, **kwargs):
        """show"""

        title = kwargs.pop("title", "")
        labels = kwargs.pop("labels", [])
        loc = kwargs.get("loc", "best")
        xlabel = kwargs.pop("xlabel", "X-axis")
        ylabel = kwargs.pop("ylabel", "Y-axis")

        plt.title(title)

        if len(labels):
            plt.legend(labels, loc=loc)

        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.show()

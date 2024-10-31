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
        xticks = kwargs.pop("xticks", None)
        yticks = kwargs.pop("yticks", None)
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

        if xticks and len(xticks):
            plt.xticks(
                [i for i, _ in enumerate(xticks)],
                [item[:3] for _, item in enumerate(xticks)],
            )

        if yticks:
            plt.yticks(yticks)

        plt.show()

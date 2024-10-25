"""OLAP_cube"""

# pylint: disable=E0401, R0914, W0611

from dataclasses import dataclass

import numpy as np
import pylab

from utils import Utils


@dataclass
class OLAPcube:
    """OLAP_cube"""

    def __init__(self, data, integro, **kwargs):
        xlabel = kwargs.pop("xlabel", "X-axis")
        ylabel = kwargs.pop("ylabel", "Y-axis")
        zlabel = kwargs.pop("zlabel", "Z-axis")
        zdir = kwargs.pop("zdir", "y")

        utils = Utils()

        data_size = np.shape(data)
        row_len = int(data_size[0])  # Рядки
        col_len = int(data_size[1])  # Колонки

        xg = np.ones(col_len)

        for i in range(col_len):
            xg[i] = i

        fig = pylab.figure()
        ax = fig.add_subplot(projection="3d")
        color = utils.gen_gradient(col_len)

        for i in range(row_len):
            ax.bar(xg, data[i], i, zdir=zdir, color=color)

        ax.bar(xg, integro, row_len, zdir=zdir, color=color)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        ax.set_zlabel(zlabel)

        pylab.show()

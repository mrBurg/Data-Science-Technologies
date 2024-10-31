"""Models"""

# pylint: disable=R0913, E0401

from dataclasses import dataclass

import numpy as np


@dataclass
class Model:
    """Models"""

    def mnk_extrapol(self, data, coef) -> np.ndarray:
        """статистичні характеристики екстраполяції"""

        data_size = len(data)
        extrapol = np.zeros((data_size + coef, 1))
        yin = np.zeros((data_size, 1))
        f = np.ones((data_size, 3))

        for i in range(data_size):
            yin[i, 0] = float(data[i])
            f[i, 1] = float(i)
            f[i, 2] = float(i * i)

        ft = f.T
        fft = ft.dot(f)
        ffti = np.linalg.inv(fft)
        fftift = ffti.dot(ft)
        c = fftift.dot(yin)

        for i in range(data_size + coef):
            extrapol[i, 0] = c[0, 0] + c[1, 0] * i + (c[2, 0] * i * i)

        return extrapol

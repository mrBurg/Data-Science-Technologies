"""Matrix"""

# pylint: disable=E0401

from dataclasses import dataclass

import numpy as np
import pandas as pd

from utils import Utils


@dataclass
class Matrix(Utils):
    """Maxtix"""

    def generation(self, data: pd.DataFrame):
        """generation"""

        title_data = data.columns
        matrix_size = np.shape(data)
        row_len = int(matrix_size[0])  # Рядки
        col_len = int(matrix_size[1])  # Колонки
        matrix_data = np.zeros((row_len, (col_len - 2)))

        for i in range(1, col_len - 1):
            file_data = self.file_parsing(title_data[i], data)
            matrix_data[:, i - 1] = file_data

        return matrix_data

    def adapter(self, data, line):
        """adapter"""

        matrix_size = np.shape(data)
        col_len = int(matrix_size[1])  # Колонки
        matrix_data = np.zeros((col_len))

        matrix_data[:] = data[line, :]

        return matrix_data

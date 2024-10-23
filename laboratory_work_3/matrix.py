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
        line_data = int(data.shape[0])  # Рядки
        column_data = int(data.shape[1])  # Колонки
        matrix_data = np.zeros((line_data, (column_data - 2)))

        for i in range(1, column_data - 1, 1):
            file_data = self.file_parsing(title_data[i], data)
            matrix_data[:, i - 1] = file_data

        return matrix_data

    def adapter(self, data, line):
        """adapter"""

        matrix_props = np.shape(data)
        matrix_data = np.zeros(matrix_props[1])

        for i in range(matrix_props[1]):
            matrix_data[i] = data[line, i]

        return matrix_data

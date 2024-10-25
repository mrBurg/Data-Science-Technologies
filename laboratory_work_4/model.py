"""Model"""

# pylint: disable=R0903, R0914, E0401

import numpy as np

from matrix import Matrix


class Model(Matrix):
    """Model"""

    def __init__(self, file_data):
        matrix = self.generation(file_data)
        matrix_size = np.shape(matrix)
        row_len = int(matrix_size[0])  # Рядки
        col_len = int(matrix_size[1])  # Колонки
        coef_prefer = np.ones(row_len)

        matrix_data = np.empty((row_len, col_len))

        for i in range(row_len):
            matrix_data[i] = self.adapter(matrix, i)

        col_name = file_data.columns[len(file_data.columns) - 1]
        criteries = file_data[col_name]

        row_sum = np.zeros(row_len)

        for i, item in enumerate(matrix_data):
            row_sum[i] = 0

            for j in item:
                if criteries[i] == "макс":
                    row_sum[i] += 1 / j

                    continue

                row_sum[i] += j

        coef_prefer_data = []
        gnorm = np.sum(coef_prefer)
        coef_prefer_data[:] = coef_prefer / gnorm

        normals = np.zeros((row_len, col_len))

        for i in range(row_len):
            for j in range(col_len):
                if criteries[i] == "макс":
                    normals[i][j] = (1 / matrix_data[i][j]) / row_sum[i]

                    continue

                normals[i][j] = matrix_data[i][j] / row_sum[i]

        integro = np.zeros(col_len)

        for i in range(col_len):
            integro[i] = 0

            for j in range(row_len):
                integro[i] += coef_prefer_data[j] * (1 - normals[j][i]) ** (-1)

        self.normals = normals
        self.integro = integro

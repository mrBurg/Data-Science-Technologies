"""Laboratory work 2"""

# pylint: disable=E1121, E0401, R0913, R0914

# import math as mt
# from pathlib import Path
from pathlib import Path
import math as mt

import numpy as np

from utils import Utils
from matrix import Matrix

matrix = Matrix()


def voronin(data_origin, data, coef_prefer):
    """Voronin"""

    matrix_size = np.shape(data)
    row_len = int(matrix_size[0])  # Рядки
    col_len = int(matrix_size[1])  # Колонки

    data_list = np.empty((row_len, col_len))

    for i in range(row_len):
        data_list[i] = matrix.adapter(data, i)

    col_name = data_origin.columns[len(data_origin.columns) - 1]
    criteries = data_origin[col_name]

    row_sum = np.zeros(row_len)

    for i, item in enumerate(data_list):
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
                normals[i][j] = (1 / data_list[i][j]) / row_sum[j]

                continue

            normals[i][j] = data_list[i][j] / row_sum[j]

    integro = np.zeros(col_len)

    for i in range(col_len):
        integro[i] = 0

        for j in range(row_len):
            integro[i] += coef_prefer_data[j] * (1 - normals[j][i]) ** (-1)

    min_val = 100
    opt = 0

    for i in range(col_len):
        if min_val > integro[i]:
            min_val = integro[i]
            opt = i

    print("Інтегрована оцінка (scor):")
    print(integro)
    print("Номер_оптимального_товару:", opt)


if __name__ == "__main__":
    root_file_path = Path(__file__).parent.joinpath("./").resolve()
    FILE_NAME = "data.xls"

    utils = Utils()

    file_data = utils.read_excel(root_file_path, FILE_NAME)
    matrix_data = matrix.generation(file_data)
    matrix_data_size = np.shape(matrix_data)
    matrix_row_len = int(matrix_data_size[0])  # Рядки

    print(file_data)
    voronin(file_data, matrix_data, np.ones(matrix_row_len))

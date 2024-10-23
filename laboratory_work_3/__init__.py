"""Laboratory work 2"""

# pylint: disable=E1121, E0401, R0913

# import math as mt
# from pathlib import Path
from pathlib import Path

import numpy as np

from utils import Utils
from matrix import Matrix

matrix = Matrix()


def voronin(data_origin, data, coef_prefer):
    """Voronin"""

    column_len = np.shape(data)[1]  # Кількість колонок

    f1f9 = []  # data_list

    for i in range(column_len):
        f1f9.append(matrix.adapter(data, i))

    g10g90 = []
    gnorm = np.sum(coef_prefer)  # coef_prefer_sum
    g10g90[:] = coef_prefer / gnorm

    column_name = data_origin.columns[len(data_origin.columns) - 1]
    criteries = data_origin[column_name]

    sum_f1_sum_f9 = []

    for item in f1f9:
        for i in range(column_len):
            if criteries[i] == "макс":
                sum_f1_sum_f9.append(1 / item[i])

                continue

            sum_f1_sum_f9.append(item[i])

    f10f90 = []  # data_dimens
    integro = np.zeros(column_len)

    for i, item in enumerate(f1f9):
        for j in range(column_len):
            if criteries[j] == "макс":
                sum_f1_sum_f9.append((1 / item[j]) / sum_f1_sum_f9[j])

                continue

            f10f90.append(item[j] / sum_f1_sum_f9[j])

            integro[j] = g10g90[j] + (1 - f10f90[i]) ** (-1)

    min_val = 10000
    opt = 0

    for i in range(column_len):
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

    voronin(file_data, matrix_data, np.ones(len(matrix_data[1])))

    # print(file_data)

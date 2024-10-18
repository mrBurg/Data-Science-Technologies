"""Laboratory work 1"""

# pylint: disable=E1121, E0401

import math as mt

from models import Model
from data_generation import DataGeneration as Data
from utils import Utils

# Закон зміни похибки – рівномірний;
# Закон зміни досліджуваного процесу – постійна.


if __name__ == "__main__":
    DATA_SIZE = 10_000
    MAX_VAL = int(DATA_SIZE)
    ABNORM_SIZE = int((MAX_VAL * 10) / 100)
    COEF = 0.000005
    COEF_PREFER = 3
    DEVIAT = 100
    MEAN = 0
    MEAN_SQRT = 3
    BINS = 50
    # # WIND = 5
    # # ALFA = 0.5

    data = Data()
    model = Model()

    # data_uniform = data.uniform(DATA_SIZE, MAX_VAL)
    # normal_data = data.normal(DATA_SIZE, DEVIAT)
    # model.hist(data_uniform, bins=BINS, label="Випадкові рівномірні дані")
    # model.plot(data_uniform, title="Випадкові дані за РІВНОМІРНИМ законом розподілу")

    normal_data = data.normal(DATA_SIZE, DEVIAT, MEAN)
    # model.hist(normal_data, bins=BINS, label="Випадкові нормальні дані")
    # model.plot(normal_data, title="Випадкові дані за НОРМАЛЬНИМ законом розподілу")

    ideal_model = model.ideal(DATA_SIZE, COEF)

    normal_model = model.normal(ideal_model, normal_data)
    # model.plot(normal_model, ideal_model, title="Модель нормального тренду")

    # abnormal_model = model.abnormal(DATA_SIZE, normal_data, COEF, MEAN, MEAN_SQRT)
    abnormal_model = model.abnormal(
        DATA_SIZE, ABNORM_SIZE, normal_data, COEF, COEF_PREFER, MEAN, MEAN_SQRT
    )
    model.plot(abnormal_model, ideal_model, title="Модель аномального тренду")

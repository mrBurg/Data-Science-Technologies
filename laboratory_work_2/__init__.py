"""Laboratory work 2"""

# pylint: disable=E1121, E0401

import math as mt

from models import Model
from data_generation import DataGeneration as Data

if __name__ == "__main__":
    DATA_SIZE = 1000
    MAX_VAL = int(DATA_SIZE)
    ABNORM_SIZE = int((MAX_VAL * 10) / 100)
    COEF = 0.001
    COEF_PREFER = 3
    DEVIAT = 10
    MEAN = 0.3
    MEAN_SQRT = 50
    BINS = 50
    # # WIND = 5
    # # ALFA = 0.5

    data = Data()
    model = Model()

    data_uniform = data.uniform(DATA_SIZE, MAX_VAL, -MAX_VAL)
    model.hist(data_uniform, bins=BINS, label="Випадкові рівномірні дані")

    ideal_model = model.ideal(DATA_SIZE, COEF)
    model.plot(
        data_uniform, ideal_model, title="Рівномірні дані + Модель ідеального тренду"
    )

    normal_model = model.normal(ideal_model, data_uniform)
    model.plot(
        normal_model, ideal_model, title="Модель нормального + ідеального тренду"
    )

    abnormal_model = model.abnormal(
        DATA_SIZE, ABNORM_SIZE, data_uniform, COEF, COEF_PREFER, MEAN, MEAN_SQRT
    )
    model.plot(
        abnormal_model, ideal_model, title="Модель анормального + ідеального тренду"
    )

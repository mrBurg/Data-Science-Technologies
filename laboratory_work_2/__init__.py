"""Laboratory work 2"""

# pylint: disable=E1121, E0401

import math as mt
from pathlib import Path

import numpy as np

from models import Model
from data_generation import DataGeneration as Data
from utils import Utils

if __name__ == "__main__":
    data = Data()
    model = Model()
    utils = Utils()

    root_file_path = Path(__file__).parent.joinpath("./").resolve()
    FILE_NAME = "Oschadbank_(USD).xls"
    DATA_NAME_NAME = "Продаж"

    file_data = utils.read_excel(root_file_path, FILE_NAME, DATA_NAME_NAME)

    DATA_SIZE = len(file_data)
    MAX_VAL = int(np.max(file_data))
    MIN_VAL = int(np.min(file_data))
    DEVIAT = 10
    ABNORM_SIZE = int((MAX_VAL * DEVIAT) / 100)
    COEF = 0.001
    COEF_PREFER = 3
    MEAN = np.mean([MIN_VAL, MAX_VAL])
    MEAN_SQRT = 3
    BINS = 20
    WIND = 5
    COEF_EXTRAPOL = mt.ceil(DATA_SIZE * 0.5)

    data_uniform = data.uniform(DATA_SIZE, MAX_VAL, MIN_VAL)
    permanent_model = model.permanent(DATA_SIZE, MEAN)

    labels = ["Рівномірні", "Постійні"]
    model.hist(
        data_uniform,
        permanent_model,
        title="Гістограма " + " + ".join(labels) + " дані",
        labels=labels,
        bins=BINS,
    )
    model.plot(
        data_uniform,
        permanent_model,
        title="Графік " + " + ".join(labels) + " дані",
        labels=labels,
    )

    abnormal_model = model.abnormal(
        data_uniform, ABNORM_SIZE, COEF, COEF_PREFER, MEAN, MEAN_SQRT
    )

    labels = ["Рівномірні", "Аномальні"]
    model.plot(
        data_uniform,
        abnormal_model,
        title="Графік " + " + ".join(labels) + " дані",
        labels=labels,
    )

    sliding_wind = model.sliding_wind(data_uniform, WIND)
    model.stat_characts_in(
        sliding_wind, title="Вибірка очищена алгоритмом sliding wind"
    )
    model.stat_characts_out(
        data_uniform,
        model.mnk(sliding_wind),
        title="Згладжена, вибірка очищена алгоритмом sliding wind",
    )

    model.qual_assess(
        sliding_wind, model.mnk(data_uniform), "Характеристики оцінювання"
    )

    extrapol = model.mnk_extrapol(sliding_wind, COEF_EXTRAPOL)
    labels = ["Прогнозування", "алгоритм sliding wind"]
    model.plot(
        sliding_wind,
        extrapol,
        title="Графік " + " + ".join(labels) + " дані",
        labels=labels,
    )

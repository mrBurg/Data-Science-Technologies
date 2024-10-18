"""Laboratory work 1"""

# pylint: disable=E1121, E0401

from models import Model
from data_generation import DataGeneration as Data


if __name__ == "__main__":
    DATA_LEN = 1000
    MAX_VAL = int(DATA_LEN)

    data = Data()
    model = Model()

    uniform_data = data.uniform(DATA_LEN, MAX_VAL, -MAX_VAL)
    model.stat_characts(
        uniform_data,
        "Статистичні характеристики випадкових даних РІВНОМІРНОГО закону розподілу",
    )
    model.hist(
        uniform_data,
        bins=20,
        label=f"Згенеровані дані від 0 до {MAX_VAL}",
    )

    permanent_data = model.permanent(DATA_LEN, MAX_VAL)
    model.stat_characts(
        permanent_data, "Статистичні характеристики ПОСТІЙНОГО закону розподілу"
    )
    model.hist(
        permanent_data,
        bins=20,
        label=f"Згенеровані дані від 0 до {MAX_VAL}",
    )

    additive = model.normal(uniform_data, permanent_data)
    model.stat_characts_in(additive, "Статистичні характеристики адитивної суміщі")
    model.plot("Модель + Постійні дані", additive, permanent_data)

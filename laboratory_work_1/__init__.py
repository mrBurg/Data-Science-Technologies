"""Laboratory work 1"""

# pylint: disable=E1121

from characts import Characts
from models import Model
from laws import Laws


if __name__ == "__main__":
    DATA_LEN = 10_000
    MAX_VAL = int(DATA_LEN)

    characts = Characts()
    laws = Laws()
    model = Model()

    even = laws.even(DATA_LEN, MAX_VAL)
    characts.all(even)
    laws.hist(even)

    normal_law = laws.normal(DATA_LEN, 0, 10)

    ideal_model = model.ideal(DATA_LEN, coef=0.001)

    normal_model = model.norm(normal_law, ideal_model)
    characts.stat_in(normal_model, "Вибірка + Норм. шум")
    laws.plot(ideal_model, normal_model, "Квадратична модель + Норм. шум")

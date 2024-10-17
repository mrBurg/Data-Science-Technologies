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
    characts.all(normal_law)
    laws.hist(normal_law)

    exponential_law = laws.exponential(DATA_LEN, 2.5)
    characts.all(exponential_law)
    laws.hist(exponential_law)

    ideal_model = model.ideal(DATA_LEN, coef=0.000001, sqrt=True)

    normal_model = model.norm(normal_law, ideal_model)
    characts.stat_in(normal_model, "Вибірка + Норм. шум")
    laws.plot(ideal_model, normal_model, "Квадратична модель + Норм. шум")

    abnormal_model = model.abnormal(even, ideal_model, normal_model, 20, 6, 25)
    characts.stat_in(abnormal_model, "Вибірка з АВ")
    laws.plot(ideal_model, abnormal_model, "Квадратична модель + Норм. шум + АВ")

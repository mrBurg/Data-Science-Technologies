"""Laboratory work 1"""

# pylint: disable=E1121

from utils import Utils
from characts import Characts
from models import Model
from laws import Laws


if __name__ == "__main__":
    DATA_LEN = 10_000
    MAX_VAL = int(DATA_LEN)

    utils = Utils()
    characts = Characts()
    laws = Laws()
    model = Model()

    even = laws.even(DATA_LEN, MAX_VAL)
    characts.all(even)
    laws.hist(even)

    normal = laws.normal(DATA_LEN, 0, 10)
    characts.all(normal)
    laws.hist(normal)

    exponential = laws.exponential(DATA_LEN, 2.5)
    laws.hist(exponential)

    ideal = model.ideal(DATA_LEN, coef=0.000001)
    norm = model.norm(normal, ideal)
    abnormal = model.abnormal(even, ideal, norm, 20, 6, 25)

    laws.plot(ideal, norm, "Квадратична модель + Норм. шум")
    characts.stat_in(norm, "Вибірка + Норм. шум")
    laws.plot(ideal, abnormal, "Квадратична модель + Норм. шум + АВ")
    characts.stat_in(norm, "Вибірка з АВ")

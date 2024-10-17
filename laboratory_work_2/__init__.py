"""Laboratory work 1"""

# pylint: disable=E1121, E0401

from characteristics import Characteristics as Chars
from models import Model
from laws import Laws
from rendering import Rendering as Rend


if __name__ == "__main__":
    DATA_LEN = 10_000
    MAX_VAL = int(DATA_LEN)
    DEVIATION = int(10)
    DSIG = 5
    COEF = 0.000001

    chars = Chars()
    laws = Laws()
    model = Model()
    rend = Rend()

    even = laws.even(DATA_LEN, MAX_VAL)
    normal_law = laws.normal(DATA_LEN, DEVIATION, 0)
    exponential_law = laws.exponential(DATA_LEN, 1.5)

    for i in (even, normal_law, exponential_law):
        chars.all(i)
        rend.hist(i)

    ideal_model = model.ideal(DATA_LEN, coef=COEF, deg=1)
    chars.stat_in(ideal_model, "Норм.")
    rend.plot("Квадратична модель + Норм. шум", "", ideal_model)

    normal_model = model.normal(normal_law, ideal_model)
    chars.stat_in(normal_model, "Вибірка + Норм. шум")
    rend.plot("Квадратична модель + Норм. шум", "", normal_model, ideal_model)

    abnormal_model = model.abnormal(
        even, ideal_model, normal_model, DATA_LEN, COEF, DSIG
    )
    chars.stat_in(abnormal_model, "Вибірка з АВ")
    rend.plot("Квадратична модель + Норм. шум + АВ", "", abnormal_model, ideal_model)

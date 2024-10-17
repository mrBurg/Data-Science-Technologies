""" Models """

from dataclasses import dataclass
import numpy as np
from config import Config

__version__ = "1.0.0"

cfg = Config(10000, 3, 10)


@dataclass
class Models:
    """Models"""

    # SAV = randomAM(n, iter)

    # def __init__(self) -> None:
    #     # SAV = randomAM(n, iter)

    #     print(vars(cfg))
    #     print(cfg.__dict__)

    def ideal_trends(self, n):
        """Модель ідеального тренду (квадратичний закон)"""

        s0 = np.zeros((n))

        for i in range(n):
            s0[i] = 0.0000005 * i * i  # квадратична модель реального процесу

        return s0

    def random_am(self, n, iter):
        """рівномірний закон розводілу номерів АВ в межах вибірки"""

        sav = np.zeros((cfg.nav))
        s = np.zeros((cfg.n))
        for i in range(n):
            s[i] = np.random.randint(
                0, iter
            )  # параметри закону задаются межами аргументу
        ms = np.median(s)
        ds = np.var(s)
        scvs = np.sqrt(ds)
        # -------------- генерація номерів АВ за рівномірним законом  -------------------
        for i in range(cfg.nav):
            sav[i] = np.ceil(
                np.random.randint(1, iter)
            )  # рівномірний розкид номерів АВ в межах вибірки розміром 0-iter
        # print("номери АВ: sav=", sav)
        # print("----- статистичны характеристики РІВНОМІРНОГО закону розподілу ВВ -----")
        # print("матиматичне сподівання ВВ=", ms)
        # print("дисперсія ВВ =", ds)
        # print("СКВ ВВ=", scvs)
        # print("-----------------------------------------------------------------------")
        # гістограма закону розподілу ВВ
        # plt.hist(S, bins=20, facecolor="blue", alpha=0.5)
        # plt.show()
        return sav

    # def measure_normal_noise(self, sn, s0n, n):
    #     """Модель виміру (квадратичний закон) з нормальний шумом"""

    #     sv = np.zeros((n))

    #     for i in range(n):
    #         sv[i] = s0n[i] + sn[i]
    #     return sv

    # def measure_anomal_winds(self, S0, SV, nAV, Q_AV):
    #     """модель виміру (квадратичний закон) з нормальний шумом + АНОМАЛЬНІ ВИМІРИ"""

    #     SV_AV = SV
    #     SSAV = np.random.normal(
    #         self.dm, (Q_AV * self.dsig), nAV
    #     )  # аномальна випадкова похибка з нормальним законом
    #     for i in range(nAV):
    #         k = int(SAV[i])
    #         SV_AV[k] = (
    #             S0[k] + SSAV[i]
    #         )  # аномальні вимірів з рівномірно розподіленими номерами
    #     return SV_AV


if __name__ == "__main__":
    models = Models()

    # S0 = models.ideal_trends(cfg.n)
    SAV = models.random_am(cfg.n, cfg.n)

    # print(S0)
    print(SAV)

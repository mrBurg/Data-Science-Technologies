"""Utils"""

from dataclasses import dataclass


@dataclass
class Utils:
    """Utils"""

    # def file_parsing(self, URL, File_name, Data_name):
    #     """File parsing"""

    #     d = pd.read_excel(File_name)
    #     for name, values in d[[Data_name]].items():
    #         print(values)
    #     S_real = np.zeros((len(values)))
    #     for i in range(len(values)):
    #         S_real[i] = values[i]

    #     print("Джерело даних: ", URL)

    #     return S_real

    # def Sliding_Window_AV_Detect_sliding_wind(S0, n_Wind):
    #     # ---- параметри циклів ----
    #     iter = len(S0)
    #     j_Wind = mt.ceil(iter - n_Wind) + 1
    #     S0_Wind = np.zeros((n_Wind))
    #     Midi = np.zeros((iter))
    #     # ---- ковзне вікно ---------
    #     for j in range(j_Wind):
    #         for i in range(n_Wind):
    #             l = j + i
    #             S0_Wind[i] = S0[l]
    #         # - Стат хар ковзного вікна --
    #         Midi[l] = np.median(S0_Wind)
    #     # ---- очищена вибірка  -----
    #     S0_Midi = np.zeros((iter))
    #     for j in range(iter):
    #         S0_Midi[j] = Midi[j]
    #     for j in range(n_Wind):
    #         S0_Midi[j] = S0[j]
    #     return S0_Midi

    # def r2_score(self, SL, Yout, Text):
    #     """Коефіцієнт детермінації - оцінювання якості моделі"""
    #     # статистичні характеристики вибірки з урахуванням тренду

    #     iter = len(Yout)
    #     numerator = 0
    #     denominator_1 = 0
    #     for i in range(iter):
    #         numerator = numerator + (SL[i] - Yout[i, 0]) ** 2
    #         denominator_1 = denominator_1 + SL[i]
    #     denominator_2 = 0
    #     for i in range(iter):
    #         denominator_2 = denominator_2 + (SL[i] - (denominator_1 / iter)) ** 2
    #     R2_score_our = 1 - (numerator / denominator_2)
    #     print("------------", Text, "-------------")
    #     print("кількість елементів вбірки=", iter)
    #     print("Коефіцієнт детермінації (ймовірність апроксимації)=", R2_score_our)

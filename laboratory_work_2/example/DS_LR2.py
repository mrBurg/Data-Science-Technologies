"""
Виконав: Руслан Карпушин

Package            Version
------------------ --------
matplotlib         3.8.3
numpy              1.26.4
pandas             2.2.1
pip                24.0
scipy              1.12.0

"""

import time
import numpy as np
import pandas as pd
import math as mt
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


# ------------------------ ФУНКЦІЯ парсингу реальних даних --------------------------


def file_parsing(URL, File_name, Data_name):
    d = pd.read_excel(File_name)
    for name, values in d[[Data_name]].items():
        print(values)
    S_real = np.zeros((len(values)))
    for i in range(len(values)):
        S_real[i] = values[i]
    print("Джерело даних: ", URL)
    return S_real


# ---------------------- ФУНКЦІЇ тестової аддитивної моделі -------------------------


# ---------------------- НОРМАЛЬНИЙ закон розподілу вхідної виборки (ВВ) ------------
def randoNORM(dm, dsig, iter):
    S = np.random.normal(
        dm, dsig, iter
    )  # нормальний закон розподілу ВВ з вибіркою єбємом iter та параметрами: dm, dsig
    mS = np.median(S)
    dS = np.var(S)
    scvS = mt.sqrt(dS)
    print("------- статистичні характеристики НОРМАЛЬНОЇ похибки вимірів -----")
    print("матиматичне сподівання ВВ=", mS)
    print("дисперсія ВВ =", dS)
    print("СКВ ВВ=", scvS)
    print("------------------------------------------------------------------")

    # гістограма закону розподілу ВВ
    plt.hist(S, bins=20, facecolor="blue", alpha=0.5)
    plt.show()
    return S


# ----- Модель ідеального тренду (косинусний закон)
def Model(n):
    x_val = np.linspace(dm, dsig, n)
    S0 = Ampl * np.cos(2 * np.pi * fR * x_val + pH)
    # plt.figure(figsize=(10, 6))
    # plt.plot(x_val, S0, color='red', label='Косинусоїдальний сигнал')
    # plt.title('Модель виміру з косинусоїдальним законом')
    # plt.legend()
    # plt.grid(True)
    # plt.show()
    return S0


# ----- модель виміру (косинусний закон) з нормальним шумом + АНОМАЛЬНІ ВИМІРИ
def Model_NORM_AV(S0, Ampl):  # (S0, SV, nAV, Q_AV):
    x_val = np.linspace(dm, dsig, n)
    # Генерування косинусоїдального сигналу з нормальним шумом
    SV_AV = np.random.normal(dm, (Q_AV * dsig), n) + S0
    # Додавання аномальних вимірів
    aV = np.random.choice(range(n), nAVv, replace=False)
    SV_AV[aV] += Ampl

    # Побудова графіка
    # plt.figure(figsize=(10, 6))
    # plt.plot(x_val, SV_AV, label='Зашумлений сигнал з аномальними вимірами')
    # plt.plot(x_val, S0, color='red', label='Косинусоїдальний сигнал')
    # plt.title('Модель виміру з косинусоїдальним законом та аномальними вимірами')
    # plt.legend()
    # plt.grid(True)
    # plt.show()

    return SV_AV


# --------------- графіки тренда, вимірів з нормальним шумом  ---------------------------
def Plot_AV(S0_L, SV_L, Text):
    plt.clf()
    plt.plot(SV_L)
    plt.plot(S0_L)
    plt.ylabel(Text)
    plt.show()
    return


# ----- статистичні характеристики вхідної вибірки  --------
def Stat_characteristics_in(SL, Text):
    # статистичні характеристики вибірки з урахуванням тренду
    Yout = MNK_Stat_characteristics(SL)
    iter = len(Yout)
    SL0 = np.zeros((iter))
    for i in range(iter):
        SL0[i] = SL[i] - Yout[i, 0]
    mS = np.median(SL0)
    dS = np.var(SL0)
    scvS = mt.sqrt(dS)
    print("------------", Text, "-------------")
    print("кількість елементів вбірки=", iter)
    print("матиматичне сподівання ВВ=", mS)
    print("дисперсія ВВ =", dS)
    print("СКВ ВВ=", scvS)
    print("-----------------------------------------------------")
    return


# ----- статистичні характеристики лінії тренда  --------
def Stat_characteristics_out(SL_in, SL, Text):
    # статистичні характеристики вибірки з урахуванням тренду
    Yout = MNK_Stat_characteristics(SL)
    iter = len(Yout)
    SL0 = np.zeros((iter))
    for i in range(iter):
        SL0[i] = SL[i, 0] - Yout[i, 0]
    mS = np.median(SL0)
    dS = np.var(SL0)
    scvS = mt.sqrt(dS)
    # глобальне лінійне відхилення оцінки - динамічна похибка моделі
    Delta = 0
    for i in range(iter):
        Delta = Delta + abs(SL_in[i] - Yout[i, 0])
    Delta_average_Out = Delta / (iter + 1)
    print("------------", Text, "-------------")
    print("кількість елементів вибірки=", iter)
    print("матиматичне сподівання ВВ=", mS)
    print("дисперсія ВВ =", dS)
    print("СКВ ВВ=", scvS)
    print("Динамічна похибка моделі=", Delta_average_Out)
    print("-----------------------------------------------------")
    return


# ------------- МНК згладжуваннядля визначення стат. характеристик -------------
def MNK_Stat_characteristics(S0):
    iter = len(S0)
    Yin = np.zeros((iter, 1))
    F = np.ones((iter, 3))
    for i in range(iter):  # формування структури вхідних матриць МНК
        Yin[i, 0] = float(S0[i])  # формування матриці вхідних даних
        F[i, 1] = float(i)
        F[i, 2] = float(i * i)
    FT = F.T
    FFT = FT.dot(F)
    FFTI = np.linalg.inv(FFT)
    FFTIFT = FFTI.dot(FT)
    C = FFTIFT.dot(Yin)
    Yout = F.dot(C)
    return Yout


# ---------------- модель виміру (квадратичний закон) з нормальним шумом ---------------
def Model_NORM(SN, S0N, n):
    SV = np.zeros((n))
    for i in range(n):
        SV[i] = S0N[i] + SN[i]
    return SV


# ------------------------ МНК детекція та очищення АВ ------------------------------
def MNK_AV_Detect(S0):
    iter = len(S0)
    Yin = np.zeros((iter, 1))
    F = np.ones((iter, 3))
    for i in range(iter):  # формування структури вхідних матриць МНК
        Yin[i, 0] = float(S0[i])  # формування матриці вхідних даних
        F[i, 1] = float(i)
        F[i, 2] = float(i * i)
    FT = F.T
    FFT = FT.dot(F)
    FFTI = np.linalg.inv(FFT)
    FFTIFT = FFTI.dot(FT)
    C = FFTIFT.dot(Yin)
    return C[1, 0]


# ------------------------------ Виявлення АВ за МНК -------------------------------------
def Sliding_Window_AV_Detect_MNK(S0, Q, n_Wind):
    # ---- параметри циклів ----
    iter = len(S0)
    j_Wind = mt.ceil(iter - n_Wind) + 1
    S0_Wind = np.zeros((n_Wind))
    # -------- еталон  ---------
    Speed_standart = MNK_AV_Detect(SV_AV)
    Yout_S0 = MNK(SV_AV)
    # ---- ковзне вікно ---------
    for j in range(j_Wind):
        for i in range(n_Wind):
            l = j + i
            S0_Wind[i] = S0[l]
        # - Стат хар ковзного вікна --
        dS = np.var(S0_Wind)
        scvS = mt.sqrt(dS)
        # --- детекція та заміна АВ --
        Speed_standart_1 = abs(Speed_standart * mt.sqrt(iter))
        Speed_1 = abs(Q * Speed_standart * mt.sqrt(n_Wind) * scvS)
        if Speed_1 > Speed_standart_1:
            # детектор виявлення АВ
            S0[l] = Yout_S0[l, 0]
    return S0


# ----- Коефіцієнт детермінації - оцінювання якості моделі --------
def r2_score(SL, Yout, Text):
    # статистичні характеристики вибірки з урахуванням тренду
    iter = len(Yout)
    numerator = 0
    denominator_1 = 0
    for i in range(iter):
        numerator = numerator + (SL[i] - Yout[i, 0]) ** 2
        denominator_1 = denominator_1 + SL[i]
    denominator_2 = 0
    for i in range(iter):
        denominator_2 = denominator_2 + (SL[i] - (denominator_1 / iter)) ** 2
    R2_score_our = 1 - (numerator / denominator_2)
    print("------------", Text, "-------------")
    print("кількість елементів вбірки=", iter)
    print("Коефіцієнт детермінації (ймовірність апроксимації)=", R2_score_our)

    return R2_score_our


# ----- Коефіцієнт детермінації - оцінювання якості моделі --------
def r2_score_expo(SL, Yout, Text):
    # статистичні характеристики вибірки з урахуванням тренду
    iter = len(Yout)
    numerator = 0
    denominator_1 = 0
    for i in range(iter):
        numerator = numerator + (SL[i] - Yout[i]) ** 2
        denominator_1 = denominator_1 + SL[i]
    denominator_2 = 0
    for i in range(iter):
        denominator_2 = denominator_2 + (SL[i] - (denominator_1 / iter)) ** 2
    R2_score_our = 1 - (numerator / denominator_2)
    print("------------", Text, "-------------")
    print("кількість елементів вбірки=", iter)
    print("Коефіцієнт детермінації (ймовірність апроксимації)=", R2_score_our)

    return R2_score_our


# ------------------------- алгоритм -а-b фільтрa ------------------------
def ABF(S0):
    iter = len(S0)
    Yin = np.zeros((iter, 1))
    YoutAB = np.zeros((iter, 1))
    T0 = 1
    for i in range(iter):
        Yin[i, 0] = float(S0[i])
    # -------------- початкові дані для запуску фільтра
    Yspeed_retro = (Yin[1, 0] - Yin[0, 0]) / T0
    Yextra = Yin[0, 0] + Yspeed_retro
    alfa = 2 * (2 * 1 - 1) / (1 * (1 + 1))
    beta = (6 / 1) * (1 + 1)
    YoutAB[0, 0] = Yin[0, 0] + alfa * (Yin[0, 0])
    # -------------- рекурентний прохід по вимірам
    for i in range(1, iter):
        YoutAB[i, 0] = Yextra + alfa * (Yin[i, 0] - Yextra)
        Yspeed = Yspeed_retro + (beta / T0) * (Yin[i, 0] - Yextra)
        Yspeed_retro = Yspeed
        Yextra = YoutAB[i, 0] + Yspeed_retro
        alfa = (2 * (2 * i - 1)) / (i * (i + 1))
        beta = 6 / (i * (i + 1))
    return YoutAB


# ------------------- вибір функціоналу статистичного навчання -----------------------
# ------------------------------ МНК згладжування ------------------------------------
def MNK(S0):
    iter = len(S0)
    Yin = np.zeros((iter, 1))
    F = np.ones((iter, 3))
    for i in range(iter):  # формування структури вхідних матриць МНК
        Yin[i, 0] = float(S0[i])  # формування матриці вхідних даних
        F[i, 1] = float(i)
        F[i, 2] = float(i * i)
    FT = F.T
    FFT = FT.dot(F)
    FFTI = np.linalg.inv(FFT)
    FFTIFT = FFTI.dot(FT)
    C = FFTIFT.dot(Yin)
    Yout = F.dot(C)
    print("Регресійна модель:")
    print("y(t) = ", C[0, 0], " + ", C[1, 0], " * t", " + ", C[2, 0], " * t^2")
    return Yout


# ------------------------------ Виявлення АВ за алгоритмом sliding window -------------------------------------
def Sliding_Window_AV_Detect_sliding_wind(S0, n_Wind):
    # ---- параметри циклів ----
    iter = len(S0)
    j_Wind = mt.ceil(iter - n_Wind) + 1
    S0_Wind = np.zeros((n_Wind))
    Midi = np.zeros((iter))
    # ---- ковзне вікно ---------
    for j in range(j_Wind):
        for i in range(n_Wind):
            l = j + i
            S0_Wind[i] = S0[l]
        # - Стат хар ковзного вікна --
        Midi[l] = np.median(S0_Wind)
    # ---- очищена вибірка  -----
    S0_Midi = np.zeros((iter))
    for j in range(iter):
        S0_Midi[j] = Midi[j]
    for j in range(n_Wind):
        S0_Midi[j] = S0[j]
    return S0_Midi


# ------------------------------ МНК експонента -------------------------------------
def MNK_exponent(S0):
    iter = len(S0)
    Yout = np.zeros((iter, 1))
    Yin = np.zeros((iter, 1))
    F = np.ones((iter, 4))
    for i in range(iter):  # формування структури вхідних матриць МНК
        Yin[i, 0] = float(S0[i])  # формування матриці вхідних даних
        F[i, 1] = float(i)
        F[i, 2] = float(i * i)
        F[i, 3] = float(i * i * i)
    FT = F.T
    FFT = FT.dot(F)
    FFTI = np.linalg.inv(FFT)
    FFTIFT = FFTI.dot(FT)
    C = FFTIFT.dot(Yin)
    c0 = C[0, 0]
    c1 = C[1, 0]
    c2 = C[2, 0]
    c3 = C[3, 0]
    a3 = 3 * (c3 / c2)
    a2 = (2 * c2) / (a3**2)
    a0 = c0 - a2
    a1 = c1 - (a2 * a3)
    print("Регресійна модель:")
    print("y(t) = ", a0, " + ", a1, " * t", " + ", a2, " * exp(", a3, " * t )")
    for i in range(iter):
        Yout[i, 0] = a0 + a1 * i + a2 * mt.exp(a3 * i)
    return Yout


# ----- статистичні характеристики екстраполяції  --------
def Stat_characteristics_extrapol(koef, SL, Text):
    # статистичні характеристики вибірки з урахуванням тренду
    Yout = MNK_Stat_characteristics(SL)
    iter = len(Yout)
    SL0 = np.zeros((iter))
    for i in range(iter):
        SL0[i] = SL[i, 0] - Yout[i, 0]
    mS = np.median(SL0)
    dS = np.var(SL0)
    scvS = mt.sqrt(dS)
    #  довірчий інтервал прогнозованих значень за СКВ
    scvS_extrapol = scvS * koef
    print("------------", Text, "-------------")
    print("кількість елементів ивбірки=", iter)
    print("матиматичне сподівання ВВ=", mS)
    print("дисперсія ВВ =", dS)
    print("СКВ ВВ=", scvS)
    print("Довірчий інтервал прогнозованих значень за СКВ=", scvS_extrapol)
    print("-----------------------------------------------------")
    return


# ----- статистичні характеристики лінії тренда  --------
def Stat_characteristics_out_expo(SL_in, SL, Text):
    # статистичні характеристики вибірки з урахуванням тренду
    Yout = MNK_Stat_characteristics(SL)
    iter = len(Yout)
    SL0 = np.zeros((iter))
    for i in range(iter):
        SL0[i] = SL[i] - Yout[i]
    mS = np.median(SL0)
    dS = np.var(SL0)
    scvS = mt.sqrt(dS)
    # глобальне лінійне відхилення оцінки - динамічна похибка моделі
    Delta = 0
    for i in range(iter):
        Delta = Delta + abs(SL_in[i] - Yout[i])
    Delta_average_Out = Delta / (iter + 1)
    print("------------", Text, "-------------")
    print("кількість елементів ивбірки=", iter)
    print("матиматичне сподівання ВВ=", mS)
    print("дисперсія ВВ =", dS)
    print("СКВ ВВ=", scvS)
    print("Динамічна похибка моделі=", Delta_average_Out)
    print("-----------------------------------------------------")
    return


# ---------------------------  МНК ПРОГНОЗУВАННЯ -------------------------------
def MNK_Extrapol(S0, koef):
    iter = len(S0)
    Yout_Extrapol = np.zeros((iter + koef, 1))
    Yin = np.zeros((iter, 1))
    F = np.ones((iter, 3))
    for i in range(iter):  # формування структури вхідних матриць МНК
        Yin[i, 0] = float(S0[i])  # формування матриці вхідних даних
        F[i, 1] = float(i)
        F[i, 2] = float(i * i)
    FT = F.T
    FFT = FT.dot(F)
    FFTI = np.linalg.inv(FFT)
    FFTIFT = FFTI.dot(FT)
    C = FFTIFT.dot(Yin)
    print("Регресійна модель:")
    print("y(t) = ", C[0, 0], " + ", C[1, 0], " * t", " + ", C[2, 0], " * t^2")
    for i in range(iter + koef):
        Yout_Extrapol[i, 0] = (
            C[0, 0] + C[1, 0] * i + (C[2, 0] * i * i)
        )  # проліноміальна крива МНК - прогнозування
    return Yout_Extrapol


# -------------------------------- Expo_scipy ---------------------------------
def Expo_Regres(Yin, bstart):
    def func_exp(x, a, b, c, d):
        print("Регресійна модель:")
        print("y(t) = ", c, " + ", d, " * t", " + ", a, " * exp(", b, " * t)")
        return a * np.exp(b * x) + c + (d * x)

    # ------ емпірічні коефіцієнти старта ------------------------------------
    aStart = bstart / 10
    bStart = bstart / 1000
    cStart = bstart + 10
    dStart = bstart / 10
    iter = len(Yin)
    x_data = np.ones((iter))
    y_data = np.ones((iter))
    for i in range(iter):
        x_data[i] = i
        y_data[i] = Yin[i]
    # popt, pcov = curve_fit(func_exp, x_data, y_data, p0=(12, 0.0012, 1200, 120))
    popt, pcov = curve_fit(
        func_exp, x_data, y_data, p0=(aStart, bStart, cStart, dStart)
    )

    return func_exp(x_data, *popt)


if __name__ == "__main__":
    # ------------------------------ Джерело вхідних даних ---------------------------

    print("Оберіть джерело вхідних даних та подальші дії:")
    print("1 - модель")
    print("2 - реальні дані")
    Data_mode = int(input("mode: "))

    if Data_mode == 1:
        # ------------------------------ сегмент констант ---------------------------------------
        n = 1000  # кількість реалізацій ВВ - об'єм вибірки
        iter = int(n)
        Q_AV = 0.05  # коефіцієнт переваги АВ
        nAVv = 10
        nAV = int(
            (iter * nAVv) / 100
        )  # кількість АВ у відсотках та абсолютних одиницях
        dm = 0
        dsig = 10  # параметри нормального закону розподілу ВВ: середнє та СКВ

        # параметри для косинусоїдального тренду
        # x_val = np.linspace(dm, dsig, n)
        fR = 0.1  # частота
        Ampl = 2  # Величина аномальних вимірів
        pH = np.pi / 4  # фаза

        # ------------------------------ СЕГМЕНТ ДАНИХ ---------------------------
        # ------------ виклики функцій моделей: тренд, аномального та нормального шуму  ----------
        S0 = Model(n)  # модель ідеального тренду (косинусоідальний закон)
        S = randoNORM(dm, dsig, iter)  # модель нормальних помилок
        SAV = S  # модель НОРМАЛЬНИХ номерів АВ

        # ----------------------------- Нормальні похибки ------------------------------------
        SV = Model_NORM(S, S0, n)  # модель тренда + нормальних помилок

        # # ----------------------------- Аномальні похибки ------------------------------------
        SV_AV = Model_NORM_AV(S0, Ampl)  # модель тренда + нормальних помилок + АВ
        Plot_AV(S0, SV_AV, "косинусна модель + Норм. шум + АВ")
        Stat_characteristics_in(SV_AV, "Вибірка з АВ")

    if Data_mode == 2:

        # SV_AV = file_parsing('https://www.oschadbank.ua/rates-archive', 'Oschadbank (USD).xls', 'Купівля')  # реальні дані
        SV_AV = file_parsing(
            "https://www.oschadbank.ua/rates-archive", "Oschadbank (USD).xls", "Продаж"
        )  # реальні дані
        # SV_AV = file_parsing('https://www.oschadbank.ua/rates-archive', 'Oschadbank (USD).xls', 'КурсНбу')  # реальні дані

        S0 = SV_AV
        n = len(S0)
        iter = int(n)  # кількість реалізацій ВВ
        Plot_AV(SV_AV, SV_AV, "Коливання курсу USD в 2022 році за даними Ощадбанк")
        Stat_characteristics_in(
            SV_AV, "Коливання курсу USD в 2022 році за даними Ощадбанк"
        )

    # ------------------- вибір функціоналу статистичного навчання -----------------------

    print("Оберіть функціонал процесів навчання:")
    print("1 - МНК згладжування")
    print("2 - МНК прогнозування")
    print("3 - МНК експонента за R&D")
    print("4 - Експонента за класикою")
    print("5 - AB фільтрація")
    mode = int(input("mode:"))

    if mode == 1:
        print("MNK згладжена вибірка очищена від АВ алгоритм sliding_wind")
        # --------------- Очищення від аномальних похибок sliding window -------------------
        n_Wind = 5  # розмір ковзного вікна для виявлення АВ
        S_AV_Detect_sliding_wind = Sliding_Window_AV_Detect_sliding_wind(SV_AV, n_Wind)
        Stat_characteristics_in(
            S_AV_Detect_sliding_wind, "Вибірка очищена від АВ алгоритм sliding_wind"
        )
        StartTime = time.time()  # фіксація часу початку обчислень
        Yout_SV_AV_Detect_sliding_wind = MNK(S_AV_Detect_sliding_wind)
        totalTime = time.time() - StartTime  # фіксація часу, на очищення від АВ
        Stat_characteristics_out(
            SV_AV,
            Yout_SV_AV_Detect_sliding_wind,
            "MNK згладжена, вибірка очищена від АВ алгоритм sliding_wind",
        )
        # --------------- Оцінювання якості моделі та візуалізація -------------------------
        r2_score(
            S_AV_Detect_sliding_wind,
            Yout_SV_AV_Detect_sliding_wind,
            "MNK_модель_згладжування",
        )
        print("totalTime =", totalTime, "s")
        Plot_AV(
            Yout_SV_AV_Detect_sliding_wind,
            S_AV_Detect_sliding_wind,
            "MNK Вибірка очищена від АВ алгоритм sliding_wind",
        )

    if mode == 2:
        print("MNK ПРОГНОЗУВАННЯ")
        # --------------- Очищення від аномальних похибок sliding window -------------------
        n_Wind = 3  # розмір ковзного вікна для виявлення АВ
        koef_Extrapol = 0.5  # коефіціент прогнозування: співвідношення інтервалу спостереження до  інтервалу прогнозування
        koef = mt.ceil(
            n * koef_Extrapol
        )  # інтервал прогнозу по кількісті вимірів статистичної вибірки
        S_AV_Detect_sliding_wind = Sliding_Window_AV_Detect_sliding_wind(SV_AV, n_Wind)
        Stat_characteristics_in(
            S_AV_Detect_sliding_wind, "Вибірка очищена від АВ алгоритм sliding_wind"
        )
        Yout_SV_AV_Detect_sliding_wind = MNK_Extrapol(S_AV_Detect_sliding_wind, koef)
        Stat_characteristics_extrapol(
            koef,
            Yout_SV_AV_Detect_sliding_wind,
            "MNK ПРОГНОЗУВАННЯ, вибірка очищена від АВ алгоритм sliding_wind",
        )
        Plot_AV(
            Yout_SV_AV_Detect_sliding_wind,
            S_AV_Detect_sliding_wind,
            "MNK ПРОГНОЗУВАННЯ: Вибірка очищена від АВ алгоритм sliding_wind",
        )

    if mode == 3:
        print("MNK ЕКСПОНЕНТА")
        # --------------- Очищення від аномальних похибок sliding window -------------------
        n_Wind = 5  # розмір ковзного вікна для виявлення АВ
        koef_Extrapol = 0.5  # коефіціент прогнозування: співвідношення інтервалу спостереження до  інтервалу прогнозування
        koef = mt.ceil(
            n * koef_Extrapol
        )  # інтервал прогнозу по кількісті вимірів статистичної вибірки
        S_AV_Detect_sliding_wind = Sliding_Window_AV_Detect_sliding_wind(SV_AV, n_Wind)
        Stat_characteristics_in(
            S_AV_Detect_sliding_wind, "Вибірка очищена від АВ алгоритм sliding_wind"
        )
        StartTime = time.time()  # фіксація часу початку обчислень
        Yout_SV_AV_Detect_sliding_wind = MNK_exponent(S_AV_Detect_sliding_wind)
        totalTime = time.time() - StartTime  # фіксація часу, на очищення від АВ
        Stat_characteristics_out(
            SV_AV,
            Yout_SV_AV_Detect_sliding_wind,
            "MNK ЕКСПОНЕНТА, вибірка очищена від АВ алгоритм sliding_wind",
        )
        # --------------- Оцінювання якості моделі та візуалізація -------------------------
        r2_score(
            S_AV_Detect_sliding_wind,
            Yout_SV_AV_Detect_sliding_wind,
            "MNK ЕКСПОНЕНТА_модель_згладжування",
        )
        print("totalTime =", totalTime, "s")
        Plot_AV(
            Yout_SV_AV_Detect_sliding_wind,
            S_AV_Detect_sliding_wind,
            "MNK ЕКСПОНЕНТА: Вибірка очищена від АВ алгоритм sliding_wind",
        )

    if mode == 4:
        print("Регресія ЕКСПОНЕНТА")
        # --------------- Очищення від аномальних похибок sliding window -------------------
        n_Wind = 5  # розмір ковзного вікна для виявлення АВ
        koef_Extrapol = 0.5  # коефіціент прогнозування: співвідношення інтервалу спостереження до  інтервалу прогнозування
        koef = mt.ceil(
            n * koef_Extrapol
        )  # інтервал прогнозу по кількісті вимірів статистичної вибірки
        S_AV_Detect_sliding_wind = Sliding_Window_AV_Detect_sliding_wind(SV_AV, n_Wind)
        Stat_characteristics_in(
            S_AV_Detect_sliding_wind, "Вибірка очищена від АВ алгоритм sliding_wind"
        )
        StartTime = time.time()  # фіксація часу початку обчислень
        Yout_SV_AV_Detect_sliding_wind = Expo_Regres(S_AV_Detect_sliding_wind, 10)
        totalTime = time.time() - StartTime  # фіксація часу, на очищення від АВ
        Stat_characteristics_out_expo(
            SV_AV,
            Yout_SV_AV_Detect_sliding_wind,
            "Регресія ЕКСПОНЕНТА, вибірка очищена від АВ алгоритм sliding_wind",
        )
        # --------------- Оцінювання якості моделі та візуалізація -------------------------
        r2_score_expo(
            S_AV_Detect_sliding_wind,
            Yout_SV_AV_Detect_sliding_wind,
            "Регресія ЕКСПОНЕНТА_модель_згладжування",
        )
        print("totalTime =", totalTime, "s")
        Plot_AV(
            Yout_SV_AV_Detect_sliding_wind,
            S_AV_Detect_sliding_wind,
            "Регресія ЕКСПОНЕНТА: Вибірка очищена від АВ алгоритм sliding_wind",
        )

    if mode == 5:
        print("ABF згладжена вибірка очищена від АВ алгоритм sliding_wind")
        # --------------- Очищення від аномальних похибок sliding window -------------------
        n_Wind = 5  # розмір ковзного вікна для виявлення АВ
        S_AV_Detect_sliding_wind = Sliding_Window_AV_Detect_sliding_wind(SV_AV, n_Wind)
        Stat_characteristics_in(
            S_AV_Detect_sliding_wind, "Вибірка очищена від АВ алгоритм sliding_wind"
        )
        Yout_SV_AV_Detect_sliding_wind = ABF(S_AV_Detect_sliding_wind)
        Stat_characteristics_out(
            SV_AV,
            Yout_SV_AV_Detect_sliding_wind,
            "ABF згладжена, вибірка очищена від АВ алгоритм sliding_wind",
        )
        # --------------- Оцінювання якості моделі та візуалізація -------------------------
        r2_score(
            S_AV_Detect_sliding_wind,
            Yout_SV_AV_Detect_sliding_wind,
            "ABF_модель_згладжування",
        )
        Plot_AV(
            Yout_SV_AV_Detect_sliding_wind,
            S_AV_Detect_sliding_wind,
            "ABF Вибірка очищена від АВ алгоритм sliding_wind",
        )

from copy import deepcopy
import os
from opfunu.cec_based.cec2020 import *
from scipy.stats import cauchy


PopSize = 100
DimSize = 10
LB = [-100] * DimSize
UB = [100] * DimSize
TrialRuns = 30
MaxFEs = 1000 * DimSize
curFEs = 0
MaxIter = int(MaxFEs / PopSize)
curIter = 0
Pop = np.zeros((PopSize, DimSize))
FitPop = np.zeros(PopSize)

FuncNum = 0

BestPop = None
BestFit = float("inf")

muF1, muF2, muF3, muF4 = 0.5, 0.5, 0.5, 0.5
muCr1, muCr2 = 0.5, 0.5


def meanL(arr):
    numer = 0
    denom = 0
    for var in arr:
        numer += var ** 2
        denom += var
    return numer / denom


def Initialization(func):
    global Pop, FitPop, curFEs, DimSize, BestPop, BestFit
    for i in range(PopSize):
        for j in range(DimSize):
            Pop[i][j] = LB[j] + (UB[j] - LB[j]) * np.random.rand()
        FitPop[i] = func(Pop[i])
    BestFit = min(FitPop)
    BestPop = deepcopy(Pop[np.argmin(FitPop)])


def ISHACDE(func):
    global Pop, FitPop, curIter, MaxIter, LB, UB, PopSize, DimSize, curFEs, BestPop, BestFit, muF1, muF2, muF3, muF4, muCr1, muCr2
    Off = np.zeros((PopSize, DimSize))
    FitOff = np.zeros(PopSize)
    F1_List, F2_List, F3_List, F4_List = [], [], [], []
    Cr1_List, Cr2_List = [], []
    c = 0.1
    sigma = 0.1
    for i in range(PopSize):
        IDX = np.random.randint(0, PopSize)
        while IDX == i:
            IDX = np.random.randint(0, PopSize)
        candi = list(range(0, PopSize))
        candi.remove(i)
        candi.remove(IDX)
        r1, r2 = np.random.choice(candi, 2, replace=False)
        if FitPop[i] < FitPop[IDX]:
            F1 = cauchy.rvs(muF1, sigma)
            while True:
                if F1 > 1:
                    F1 = 1
                    break
                elif F1 < 0:
                    F1 = cauchy.rvs(muF1, sigma)
                break
            F2 = cauchy.rvs(muF2, sigma)
            while True:
                if F2 > 1:
                    F2 = 1
                    break
                elif F2 < 0:
                    F2 = cauchy.rvs(muF2, sigma)
                break
            Off[i] = Pop[i] + F1 * (BestPop - Pop[i]) + F2 * (Pop[r1] - Pop[r2])
            jrand = np.random.randint(0, DimSize)
            Cr1 = np.clip(np.random.normal(muCr1, sigma), 0, 1)
            for j in range(DimSize):
                if np.random.rand() < Cr1 or j == jrand:
                    pass
                else:
                    Off[i][j] = Pop[i][j]

                if Off[i][j] > UB[j] or Off[i][j] < LB[j]:
                    Off[i][j] = np.random.uniform(LB[j], UB[j])

            FitOff[i] = func(Off[i])
            if FitOff[i] < FitPop[i]:
                F1_List.append(F1)
                F2_List.append(F2)
                Cr1_List.append(Cr1)
                Pop[i] = deepcopy(Off[i])
                FitPop[i] = FitOff[i]
                if FitOff[i] < BestFit:
                    BestFit = FitOff[i]
                    BestPop = deepcopy(Off[i])
        else:
            F3 = cauchy.rvs(muF3, sigma)
            while True:
                if F3 > 1:
                    F3 = 1
                    break
                elif F3 < 0:
                    F3 = cauchy.rvs(muF3, sigma)
                break
            F4 = cauchy.rvs(muF4, sigma)
            while True:
                if F4 > 1:
                    F4 = 1
                    break
                elif F4 < 0:
                    F4 = cauchy.rvs(muF4, sigma)
                break
            Off[i] = Pop[IDX] + F3 * (BestPop - Pop[IDX]) + F4 * (Pop[r1] - Pop[r2])
            jrand = np.random.randint(0, DimSize)

            Cr2 = np.clip(np.random.normal(muCr2, sigma), 0, 1)
            for j in range(DimSize):
                if np.random.rand() < Cr2 or j == jrand:
                    pass
                else:
                    Off[i][j] = Pop[i][j]

                if Off[i][j] > UB[j] or Off[i][j] < LB[j]:
                    Off[i][j] = np.random.uniform(LB[j], UB[j])
            FitOff[i] = func(Off[i])
            if FitOff[i] < FitPop[i]:
                F3_List.append(F3)
                F4_List.append(F4)
                Cr2_List.append(Cr2)
                Pop[i] = deepcopy(Off[i])
                FitPop[i] = FitOff[i]
                if FitOff[i] < BestFit:
                    BestFit = FitOff[i]
                    BestPop = deepcopy(Off[i])

    if len(F1_List) == 0:
        pass
    else:
        muF1 = (1 - c) * muF1 + c * meanL(F1_List)
    if len(F2_List) == 0:
        pass
    else:
        muF2 = (1 - c) * muF2 + c * meanL(F2_List)
    if len(F3_List) == 0:
        pass
    else:
        muF3 = (1 - c) * muF3 + c * meanL(F3_List)
    if len(F4_List) == 0:
        pass
    else:
        muF4 = (1 - c) * muF4 + c * meanL(F4_List)
    if len(Cr1_List) == 0:
        pass
    else:
        muCr1 = (1 - c) * muCr1 + c * np.mean(Cr1_List)
    if len(Cr2_List) == 0:
        pass
    else:
        muCr2 = (1 - c) * muCr2 + c * np.mean(Cr2_List)


def RunISHACDE(func):
    global curFEs, curIter, MaxIter, TrialRuns, Pop, FitPop, DimSize, BestPop, muF1, muF2, muF3, muF4, muCr1, muCr2
    All_Trial_Best = []
    for i in range(TrialRuns):
        Best_list = []
        curIter = 0
        muF1, muF2, muF3, muF4 = 0.5, 0.5, 0.5, 0.5
        muCr1, muCr2 = 0.5, 0.5
        np.random.seed(2024 + 88 * i)
        Initialization(func)
        Best_list.append(min(FitPop))
        while curIter < MaxIter:
            ISHACDE(func)
            curIter += 1
            Best_list.append(min(FitPop))
        All_Trial_Best.append(Best_list)
    np.savetxt("./ISHACDE_Data/CEC2020/" + str(DimSize) + "D/F" + str(FuncNum) + ".csv", All_Trial_Best, delimiter=",")


def main(Dim):
    global FuncNum, DimSize, Pop, LB, UB, MaxIter, MaxFEs

    DimSize = Dim
    CEC2020 = [F12020(DimSize), F22020(DimSize), F32020(DimSize), F42020(DimSize), F52020(DimSize),
               F62020(DimSize), F72020(DimSize), F82020(DimSize), F92020(DimSize), F102020(DimSize)]
    LB, UB = [-100] * Dim, [100] * Dim
    MaxFEs = 1000 * DimSize
    MaxIter = int(MaxFEs / PopSize)
    Pop = np.zeros((PopSize, DimSize))
    for i in range(len(CEC2020)):
        FuncNum = i + 1
        RunISHACDE(CEC2020[i].evaluate)


if __name__ == "__main__":
    if os.path.exists('ISHACDE_Data/CEC2020/10D') == False:
        os.makedirs('ISHACDE_Data/CEC2020/10D')
    if os.path.exists('ISHACDE_Data/CEC2020/30D') == False:
        os.makedirs('ISHACDE_Data/CEC2020/30D')
    if os.path.exists('ISHACDE_Data/CEC2020/50D') == False:
        os.makedirs('ISHACDE_Data/CEC2020/50D')
    if os.path.exists('ISHACDE_Data/CEC2020/100D') == False:
        os.makedirs('ISHACDE_Data/CEC2020/100D')
    for dim in [100]:
        main(dim)

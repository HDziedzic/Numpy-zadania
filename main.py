# zadania numpy
import numpy as np


def zad_1():
    a = np.arange(3, 15 * 3 + 1, 3)
    print(a)


def zad_2():
    a = np.array([1.3, 2.5, 5.2, 6.13, 5.8], dtype=float)
    a_copy = np.copy(a).astype(dtype='int64')
    print(type(a[1]))
    print(type(a_copy[1]))
    print(a_copy)


def zad_3(n):
    a = np.matrix(np.arange(n * n).reshape((n, n))) + 1
    print(a)


def zad_4(n, x):
    a = np.logspace(1, x, num=x, base=n, dtype='int32')
    print(a)


def zad5(n):
    a = np.arange(n)
    adiag = np.diag(a[::-1])
    print(adiag)


def zad6():
    tab = np.array([['a', 'r', 'e', 'k'], ['z', 'i', ' ', ' '], ['y', ' ', 'n', ' '], ['l', ' ', ' ', 'a']])

    print(tab)


def zad7(n):
    a = np.diag([2] * n)
    for i in range(n):
        for j in range(n - 1):
            if a[i][j] != 0:
                a[i][j + 1] = a[i][j] + 2
    b = a.T
    for i in range(n):
        for j in range(n):
            if b[i][j] == 2:
                b[i][j] = 1
    print(a + b)


def zad8(tab, k):
    temp = 0
    tabc = tab
    print(tab)
    if k == 'poziom':
        b = int((tab.shape[0] / 2))
        if b % 2 == 0:
            print(tab[b:])
        else:
            print("ilość wierszy nie pozwala na tę operację")
    elif k == 'pion':
        b = int((tab.shape[1] / 2))
        if b % 2 == 0:
            while temp < b:
                tabc = np.delete(tabc, 0, axis=1)
                temp += 1
            print(tabc)
        else:
            print("ilość kolumn nie pozwala na tę operację")


# ----------------------------------------------------------------
#  ------------------do zadania 8 --------------------------------
# c = np.array([[5, 2, 4, 1], [5, 2, 4, 1], [5, 2, 4, 1]])
# k1 = 'pion'
# k2 = 'poziom'
# zad8(c, k1)
# ------------------do zadania 8 ---------------------------------
# ----------------------------------------------------------------


def zad9():
    list = [0, 1]
    for i in range(25 - 2):
        list.append(list[i] + list[(i + 1)])
    result = np.matrix(list).reshape(5, 5)
    print(result)


zad9()

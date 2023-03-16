import csv
from random import randint
from time import perf_counter
import matplotlib.pyplot as plt
import numpy as np


def t1():
    inter1 = [randint(-50, 50) for _ in range(10 ** 6)]
    inter2 = [randint(-50, 50) for _ in range(10 ** 6)]
    np_mass1 = np.array(inter1)
    np_mass2 = np.array(inter2)

    t_start1 = perf_counter()
    for i in range(10 ** 6):
        inter1[i] *= inter2[i]
    t_all1 = perf_counter() - t_start1

    t_start2 = perf_counter()
    np.multiply(np_mass1, np_mass2)
    t_all2 = perf_counter() - t_start2

    print(f'время перемножения стандартных списков - {t_all1}')
    print(f'время перемножения numpy массивов - {t_all2}')
    print(f'разница во времени - {t_all1 - t_all2}')


def hist1():
    arr = np.genfromtxt('data2.csv', delimiter=',', skip_header=1)[:, 4]
    column = arr[np.isfinite(arr)]
    fig = plt.figure(figsize=(6, 4))
    ox = fig.add_subplot()
    ox.set_title('гистограмма')
    ox.set_xlabel('интервалы')
    ox.set_ylabel('колличество значений, попавших в заданые интервалы')
    ox.hist(column, 16)
    ox.grid()

def hist2():
    arr = np.genfromtxt('data2.csv', delimiter=',', skip_header=1)[:, 4]
    column = arr[np.isfinite(arr)]

    fig = plt.figure(figsize=(6, 4))
    ox1 = fig.add_subplot()
    ox1.set_title('нормализованная гистограмма')
    ox1.hist(column, 16, density=True)
    ox1.set_xlabel('интервалы')
    ox1.set_ylabel('вероятность')
    ox1.grid()

    plt.show()

    print(f'среднеквадратическое отклонение - {np.std(column)}')


def plot3d():
    xs = np.linspace(-3 * np.pi, 3 * np.pi, 50)

    def fn(x):
        return x * np.cos(x)

    ys = np.array([fn(xi) for xi in xs])
    zs = np.sin(xs)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_xlabel('Ox')
    ax.set_ylabel('Oy')
    ax.set_zlabel('Oz')
    ax.set_title('трёхмерный график')
    ax.plot(xs, ys, zs, marker='x', c='red')
    plt.show()


t1()
plot3d()
hist1()
hist2()

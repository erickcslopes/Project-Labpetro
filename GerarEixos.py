import numpy as np


def gerar_eixos(duration, temps):
    total_time = np.sum(duration)

    t = np.array([float(i) for i in range(total_time + 1)])
    T = np.zeros_like(t)

    cur_time = 0
    old_time = 0

    for i in range(len(temps)):
        cur_time += duration[i]
        T[old_time:cur_time + 1] = temps[i]
        old_time = cur_time

    return t, T
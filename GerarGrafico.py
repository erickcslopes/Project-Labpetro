from cProfile import label
import matplotlib.pyplot as plt
import numpy as np
import time

def gerar_grafico(t, T_step, T_cont, pres, pos,dts, lab, vaz):
    fig, ax1 = plt.subplots(figsize=(12, 6))
    ax2 = ax1.twinx()


    if dts == 'ON\n':
        ax1.plot(t, T_step, color='b', label='T - DTS')
    if lab == 'ON\n':
        ax1.plot(t, T_cont, color='r', label='T - LabView')
    if vaz == 'ON\n':
        ax2.plot(t, pres, color='g', label='Vazão')

    ax1.set_xlabel('Tempo')

    ax1.set_ylabel('Temperatura (°C)', color='tab:purple')
    ax2.set_ylabel('Vasão', color='tab:green')

    fig.suptitle('DTS & LV')

    legend = [time.strftime('%H:%M:%S', time.gmtime(ti)) for ti in pos]
    ax1.set_xticks(pos, labels=legend, rotation=45)
    ax1.grid()
    ax1.legend(loc='upper left')
    ax2.legend(loc='upper right')
    plt.show()
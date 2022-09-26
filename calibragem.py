from LeituraDados import *
import numpy as np

def offset_PT100():

    log = leitura_dados_lv("log_lv/calibragem/")

    Tini = log[0]
    Tmeio = log[1]
    Tfim = log[2]

    for a in range(100):
        Tini.pop(a)
        Tmeio.pop(a)
        Tfim.pop(a)

    Media_ini = np.mean(Tini)
    Media_meio = np.mean(Tmeio)
    Media_fim = np.mean(Tfim)

    # print(Media_ini,Media_meio,Media_fim)

    if Media_fim > Media_ini:
        offset_ini = Media_fim - Media_ini
    else:
        offset_ini =  Media_fim -Media_ini

    if Media_fim > Media_meio:
        offset_meio =  Media_fim - Media_meio
    else:
        offset_meio = Media_fim - Media_meio

    return offset_ini, offset_meio

offset_amb = offset_PT100()[0]
offset_fib = offset_PT100()[1]

def calibragem (ambiente, fibra):

    for item in range(len(ambiente)):
        ambiente[item] = round((ambiente[item] + offset_amb), 2)
        fibra[item] = round((fibra[item] + offset_fib), 2)

    return ambiente, fibra

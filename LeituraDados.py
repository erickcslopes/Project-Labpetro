import re
import numpy as np
from os import listdir
from os.path import isfile, join

def to_second(form):
    h, m, s = map(int, form.split(':'))
    return h * 60 * 60 + m * 60 + s

def clean(term):
    return re.sub("[^\d\.]", "", term)

def clean_listas(origin, LM, LT):
    for x in origin:
        a = list(x.replace("\t", "@"))
        a = a[:-2]
        b = ''.join(a)
        c = b.split('@')
        LM.append(float(c[0]))
        LT.append(float(c[1]))

def leitura_dados_dts(ini,fim,point,stp):
    mypath = 'logs/'

    a = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    b = []
    for item in a:
        if ".txt" in item:
            b.append(item)

    #-----------------------------------
    #sequencia de logs
    logs = sorted(b)
    #-----------------------------------

    temperaturas = []
    duration_list = []
    data_list = []
    hora_list = []

    for log in logs:

        #-----------------------------------
        #Abertura do log
        with open(mypath + log, encoding='iso-8859-1') as f:
            lines = f.readlines()

        #-----------------------------------
        #Pescar linha especifica
        list_lines = list(lines)

        # -----------------------------------
        # Data e hora
        data = clean(list_lines[10])[:-6]
        data_list.append(data)
        hora = clean(list_lines[10])[8:]
        hora_list.append(hora)

        # -----------------------------------
        # Duração esegundos convertida para minutos
        duration = int(float(clean(list_lines[11])))
        duration_list.append(duration)

        #-----------------------------------
        #remoção de cabeçalho
        del list_lines[0:41]

        #-----------------------------------
        #separa as colunas de Temperatura x Metro
        clean_Tempe = []
        clean_Metro = []

        clean_listas(list_lines, clean_Metro, clean_Tempe)

        #-----------------------------------
        # section
        lista_sec_Metro = []
        lista_sec_Tempe = []

        if point == 0:
            for x in clean_Metro:
                location = []
                if x >= ini and x <= fim + 1:
                    lista_sec_Metro.append(x)
                    location.append(clean_Metro.index(x))
                for y in location:
                    lista_sec_Tempe.append(clean_Tempe[y])
            temperaturas.append(np.mean(lista_sec_Tempe))
        else:
            for x in clean_Metro:
                location = []
                if x <= point + 0.1 and x >= point - 0.1:
                    lista_sec_Metro.append(x)
                    location.append(clean_Metro.index(x))
                for y in location:
                    lista_sec_Tempe.append(clean_Tempe[y])
            temperaturas.append(np.mean(lista_sec_Tempe))

    if stp == 0:
        return duration_list, temperaturas
    else:
        duration_stp = []
        for x in duration_list:
            duration_stp.append(stp * 60)
        return duration_stp, temperaturas

def leitura_dados_lv(t: np.ndarray):
    T_cont = 30 - 10 * np.sin(2 * np.pi * t / 500)
    pres = np.cos(2 * np.pi * t / 871) + 4.5

    return T_cont, pres
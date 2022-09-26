import numpy as np
from funcoes import *
from os import listdir
from os.path import isfile, join
import Save

def leitura_dados_dts(ini,fim,point,stp):
    mypath = 'logs_dts/'

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

            Save.save_log(f'{Save.save_open()[2]}',f'{temperaturas}')

    if stp == 0:
        return duration_list, temperaturas
    else:
        duration_stp = []
        for x in duration_list:
            duration_stp.append(stp * 60)
        return duration_stp, temperaturas

def leitura_dados_lv(path_lv):

    ambiente = [] # T meio
    fibra = [] # T inicio
    T_fim = []
    tempo = []
    ##################################################
    a = [f for f in listdir(path_lv) if isfile(join(path_lv, f))]
    b = []

    for item in a:
        if ".txt" in item:
            b.append(item)

    ##################################################
    # sequencia de logs
    logs = sorted(b)
    ##################################################

    for log in logs:
        # -----------------------------------
        # Abertura do log
        with open(path_lv + log, encoding='iso-8859-1') as f:
            lines = f.readlines()

        # -----------------------------------
        # Pescar linha especifica
        list_lines = list(lines)

        del list_lines[0:23]

        for masure in list_lines:
            line = masure.split('\n')
            data = line[0].split('\t')
            tempo.append(comma_to_dot(data[0]))
            fibra.append(comma_to_dot(data[1]))
            ambiente.append(comma_to_dot(data[3]))
            T_fim.append(comma_to_dot(data[5]))

    return ambiente, fibra, T_fim, len(tempo)





import re
import numpy as np

def to_second(form):
    h, m, s = map(int, form.split(':'))
    return h * 60 * 60 + m * 60 + s

def clean(term):
    return re.sub("[^\d\.]", "", term)

def clean_comma(term):
    a = re.sub(",", ".", term)
    b = float(a)
    return b

def comma_to_dot(term):
    x = re.sub(",", ".", term)
    y = re.findall(r'\d+\.\d+', x)
    return round(float(y[0]), 2)

def clean_listas(origin, LM, LT):
    for x in origin:
        a = list(x.replace("\t", "@"))
        a = a[:-2]
        b = ''.join(a)
        c = b.split('@')
        LM.append(float(c[0]))
        LT.append(float(c[1]))

def normalize_fiber(ambiente, fibra, lista):
    m_ambiente = np.mean(ambiente)
    m_fibra = np.mean(fibra)
    difereca = m_ambiente - m_fibra

    for item in range(len(lista)):
        lista[item] = round((lista[item] + difereca),2)

    return lista, round(m_ambiente,2)

def divider(dados, tabela):
    number = round(len(dados)/tabela)

    def medias(list):
        temp_list = []
        count = 0
        for x in list:
            if count < number:
                temp_list.append(x)
                list.pop(0)
                count = count +1

        media = np.mean(temp_list)
        return round(float(media), 2)

    new_dados = []

    for a in range(tabela):
        new_dados.append(medias(dados))

    return new_dados

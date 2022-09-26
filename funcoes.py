import re
from os import listdir
from os.path import isfile, join


def to_second(form):
    h, m, s = map(int, form.split(':'))
    return h * 60 * 60 + m * 60 + s

def clean(term):
    return re.sub("[^\d\.]", "", term)

def clean_comma(term):
    a = re.sub(",", ".", term)
    b = float(a)
    return b

def clean_listas(origin, LM, LT):
    for x in origin:
        a = list(x.replace("\t", "@"))
        a = a[:-2]
        b = ''.join(a)
        c = b.split('@')
        LM.append(float(c[0]))
        LT.append(float(c[1]))


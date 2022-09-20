from LeituraDados import *
from GerarEixos import gerar_eixos
from GerarGrafico import gerar_grafico
from Save import *


def start_dts_lv(ponto):
    print('start')
    ini = int(save_open()[0])
    fim = int(save_open()[1])
    stp = int(save_open()[3])
    point = ponto

    duracoes, temperaturas = leitura_dados_dts(ini, fim, point, stp)

    # legendas em pontos específicos (durações)
    # pos = np.concatenate(([0], np.cumsum(duracoes)))

    # legendas com distanciamento de 5 min
    pos = np.arange(0, np.sum(duracoes), 5 * 60)

    # 10 legendas igualmente espaçadas
    # pos = np.linspace(0, np.sum(duracoes), 10)

    t, T_step = gerar_eixos(duracoes, temperaturas)
    T_cont, pres = leitura_dados_lv(t)

    dts = (save_open()[4])
    lab = (save_open()[5])
    vaz = (save_open()[6])
    gerar_grafico(t, T_step, T_cont, pres, pos, dts, lab, vaz)


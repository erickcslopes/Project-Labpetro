from LeituraDados import *

from Painel import *
from GerarEixos import gerar_eixos
from GerarGrafico import gerar_grafico
from Save import *

def start_dts_graphc(ponto):
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
    T_cont, pres = leitura_dummie(t)
    print('aaaaaa', len(T_cont),len(pres), len(t))
    print(len(leitura_dados_lv("log_lv/")[1]))

    dts = (save_open()[4])
    lab = (save_open()[5])
    vaz = (save_open()[6])
    # T_cont = 1
    # pres = 1
    gerar_grafico(t, T_step, T_cont, pres, pos, dts, lab, vaz)

from calibragem import *
def start_log_tabela(log_lv,log_lv_amb):

    ambiente_medicao = calibragem(leitura_dados_lv(log_lv)[0], leitura_dados_lv(log_lv)[1])[0]
    fibra_medicao = calibragem(leitura_dados_lv(log_lv)[0], leitura_dados_lv(log_lv)[1])[1]

    ambiente_base = calibragem(leitura_dados_lv(log_lv_amb)[0], leitura_dados_lv(log_lv_amb)[1])[0]
    fibra_base = calibragem(leitura_dados_lv(log_lv_amb)[0], leitura_dados_lv(log_lv_amb)[1])[1]

    fibra_normal = normalize_fiber(ambiente_base, fibra_base, fibra_medicao)[0]

    ambiente = ambiente_medicao
    fibra = fibra_normal

    # print(fibra)

    print('ambiente', divider(ambiente, 19))
    print('fibra', divider(fibra, 19))

    return ambiente, fibra

def start_dts_lv(ponto):

    start_dts_graphc(ponto)

def start_painel():
    interface()


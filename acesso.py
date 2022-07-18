from descricao_em_branco_exception import DescricaoEmBrancoException
from estacionamento import Estacionamento
import math

class Acesso:
    def __init__(self, horaEntrada = '', horaSaida = '', placa = '', isEvento = 0) -> None:
        if (horaEntrada.strip(' ') == ''):
            raise DescricaoEmBrancoException('Hora de Entrada')
        if (horaSaida.strip(' ') == ''):
            raise DescricaoEmBrancoException('Hora de Saída')
        if (placa.strip(' ') == ''):
            raise DescricaoEmBrancoException('Placa')
        self.horaEntrada = horaEntrada
        self.horaSaida = horaSaida
        self.placa = placa
        self.isEvento = isEvento
        self.totalArrecadado = 0

    def calculaAcesso(self, estacionamento: Estacionamento):
        if self.isEvento:
            return 40
        elif self.useDiariaNoturna(estacionamento.entrada_noturna, estacionamento.retirada_noturna):
            return estacionamento.diaria_noturna
        elif self.calculoHoras(self.horaEntrada, self.horaSaida) <= 540:
            return self.getPrecoHoraCheia(estacionamento.valor_fracao, estacionamento.valor_hora)

    def getPrecoHoraCheia(self, f_valor, v_hora):
        horas = 60 * (int(self.horaSaida.split(':')[0]) - int(self.horaEntrada.split(':')[0]))
        minutos = (int(self.horaSaida.split(':')[1]) - int(self.horaEntrada.split(':')[1]))
        tempoTotal = horas + minutos
        
        valor_total = (4*  f_valor* math.floor(tempoTotal/60))
        return valor_total - (v_hora/100) * valor_total

    def calculoHoras(self, hora1, hora2):
        horas = 60 * (int(hora2.split(':')[0]) - int(hora1.split(':')[0]))
        minutos = (int(hora2.split(':')[1]) - int(hora1.split(':')[1]))
        tempoTotal = horas + minutos
        return tempoTotal

    def useDiariaNoturna(self, entrada_noturna, retirada_noturna):
        return ((self.calculoHoras(self.horaEntrada, entrada_noturna) <= 0
                or self.calculoHoras(self.horaEntrada, retirada_noturna) > 0)
            and (self.calculoHoras(self.horaSaida, entrada_noturna) <= 0
                or self.calculoHoras(self.horaSaida, retirada_noturna) > 0))
        
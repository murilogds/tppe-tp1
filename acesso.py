from traitlets import Int
from exceptions import DescricaoEmBrancoException
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
        tempoEstacionado = self.calculoHoras(self.horaEntrada, self.horaSaida)
        if self.isEvento:
            self.totalArrecadado += estacionamento.valor_evento
            return estacionamento.valor_evento
        elif self.useDiariaNoturna(estacionamento.entrada_noturna, estacionamento.retirada_noturna):
            self.totalArrecadado += estacionamento.diaria_noturna
            return estacionamento.diaria_noturna
        elif tempoEstacionado < 540:
            valorHoraCheia = self.getPrecoHoraCheia(estacionamento.valor_fracao, estacionamento.valor_hora, tempoEstacionado)
            valorFracionado = self.getPrecoHoraFracionada(tempoEstacionado, estacionamento)
            self.totalArrecadado += valorFracionado + valorHoraCheia
            return valorFracionado + valorHoraCheia
        elif tempoEstacionado >= 540:
            valorDiariaDiurna = self.useDiariaDiurna(estacionamento)
            self.totalArrecadado += valorDiariaDiurna
            return valorDiariaDiurna

    def getPrecoHoraFracionada(self, tempoEstacionado: Int, estacionamento: Estacionamento):
        tempoFracionado = tempoEstacionado % 60 # Quantos minutos
        fracoes = math.ceil(tempoFracionado / 15)
        return fracoes * estacionamento.valor_fracao


    def getPrecoHoraCheia(self, f_valor, v_hora, tempoTotal):
        valor_total = (4*  f_valor* math.floor(tempoTotal/60))
        return valor_total - (v_hora/100) * valor_total

    def calculoHoras(self, hora1, hora2):
        horas = 60 * (int(hora2.split(':')[0]) - int(hora1.split(':')[0]))
        minutos = (int(hora2.split(':')[1]) - int(hora1.split(':')[1]))
        tempoTotal = horas + minutos
        return tempoTotal

    def useDiariaDiurna(self, estacionamento: Estacionamento):
        return estacionamento.diaria_diurna
    
    def useDiariaNoturna(self, entrada_noturna, retirada_noturna):
        return ((self.calculoHoras(self.horaEntrada, entrada_noturna) <= 0
                or self.calculoHoras(self.horaEntrada, retirada_noturna) > 0)
            and (self.calculoHoras(self.horaSaida, entrada_noturna) <= 0
                or self.calculoHoras(self.horaSaida, retirada_noturna) > 0))
    
    def getValorContratante(self, estacionamento: Estacionamento):
        return self.totalArrecadado * estacionamento.retornoContratante
        
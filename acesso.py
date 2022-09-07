from exceptions import IntervaloInvalidoException
from estacionamento import Estacionamento
from calcula_acesso import CalculaAcesso
import math

class Acesso:
    def __init__(self, horaEntrada = '', horaSaida = '', placa = '', isEvento = 0, isMensalista = 0) -> None:
        self.horaEntrada = horaEntrada
        self.horaSaida = horaSaida
        self.placa = placa
        self.isEvento = isEvento
        self.totalArrecadado = 0
        self.isMensalista = isMensalista
        self.HORA_MINUTO = 60
        self.QUARTO_DE_HORA = 15

    def calculaAcesso(self, estacionamento: Estacionamento):
        return CalculaAcesso(self).calculaAcesso(estacionamento)

    def getPrecoHoraFracionada(self, tempoEstacionado: int, estacionamento: Estacionamento):
        tempoFracionado = tempoEstacionado % self.HORA_MINUTO # Quantos minutos
        fracoes = math.ceil(tempoFracionado / self.QUARTO_DE_HORA)
        return fracoes * estacionamento.valor_fracao


    def getPrecoHoraCheia(self, f_valor, v_hora, tempoTotal):
        valor_total = (4*  f_valor* math.floor(tempoTotal/self.HORA_MINUTO))
        return valor_total - (v_hora/100) * valor_total

    def calculoHoras(self, hora1, hora2):
        horas = self.HORA_MINUTO * (int(hora2.split(':')[0]) - int(hora1.split(':')[0]))
        minutos = (int(hora2.split(':')[1]) - int(hora1.split(':')[1]))
        tempoTotal = horas + minutos
        return tempoTotal

    def useDiariaDiurna(self, estacionamento: Estacionamento):
        return estacionamento.diaria_diurna
    
    def useDiariaNoturna(self, entrada_noturna, retirada_noturna):
        return (self.entradaNoturna(entrada_noturna, retirada_noturna) 
            and self.saidaNoturna(entrada_noturna, retirada_noturna))

    def entradaNoturna(self, entrada_noturna, retirada_noturna):
        return (self.calculoHoras(self.horaEntrada, entrada_noturna) <= 0
            or self.calculoHoras(self.horaEntrada, retirada_noturna) > 0)

    def saidaNoturna(self, entrada_noturna, retirada_noturna):
        return (self.calculoHoras(self.horaSaida, entrada_noturna) <= 0
            or self.calculoHoras(self.horaSaida, retirada_noturna) > 0)

    def getValorContratante(self, estacionamento: Estacionamento):
        return self.totalArrecadado * estacionamento.retorno_contratante

    def isHorarioInvalido(self, horarioMinimo, horarioMaximo):
        return (self.calculoHoras(horarioMinimo, self.horaEntrada) < 0
            or self.calculoHoras(horarioMinimo, self.horaSaida) < 0 
            or self.calculoHoras(horarioMaximo, self.horaEntrada) > 0 
            or self.calculoHoras(horarioMaximo, self.horaSaida) > 0)
        
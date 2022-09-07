from estacionamento import Estacionamento
from exceptions import IntervaloInvalidoException

class CalculaAcesso():
    def __init__(self,acesso):
        self.acesso = acesso

    def calculaAcesso(self,estacionamento: Estacionamento):
        if self.acesso.isEvento:
            self.acesso.totalArrecadado += estacionamento.valor_evento
            return estacionamento.valor_evento
        elif self.acesso.isMensalista:
            self.acesso.totalArrecadado += estacionamento.valor_mensalista
            return estacionamento.valor_mensalista

        if self.acesso.isHorarioInvalido(estacionamento.horario_min_funcionamento, estacionamento.horario_max_funcionamento):
            raise IntervaloInvalidoException()

        tempoEstacionado = self.acesso.calculoHoras(self.acesso.horaEntrada, self.acesso.horaSaida)
        if self.acesso.useDiariaNoturna(estacionamento.entrada_noturna, estacionamento.retirada_noturna):
            self.acesso.totalArrecadado += estacionamento.diaria_noturna
            return estacionamento.diaria_noturna
        elif tempoEstacionado < 540:
            valorHoraCheia = self.acesso.getPrecoHoraCheia(estacionamento.valor_fracao, estacionamento.valor_hora, tempoEstacionado)
            valorFracionado = self.acesso.getPrecoHoraFracionada(tempoEstacionado, estacionamento)
            self.acesso.totalArrecadado += valorFracionado + valorHoraCheia
            return valorFracionado + valorHoraCheia
        elif tempoEstacionado >= 540:
            valorDiariaDiurna = self.acesso.useDiariaDiurna(estacionamento)
            self.acesso.totalArrecadado += valorDiariaDiurna
            return valorDiariaDiurna
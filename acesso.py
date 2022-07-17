from estacionamento import Estacionamento

class Acesso:
    def __init__(self, horaEntrada = '', horaSaida = '', placa = '') -> None:
        self.horaEntrada = horaEntrada
        self.horaSaida = horaSaida
        self.placa = placa

    def calculaAcesso(self, estacionamento: Estacionamento):
        if self.useDiariaNoturna(estacionamento.entrada_noturna):
            return estacionamento.diaria_noturna
        elif self.calculoHoras(self.horaEntrada, self.horaSaida) <= 540:
            return self.getPrecoHoraCheia(estacionamento.valor_fracao, estacionamento.valor_hora)

    def getPrecoHoraCheia(self, f_valor, v_hora):
        horas = 60 * (int(self.horaSaida.split(':')[0]) - int(self.horaEntrada.split(':')[0]))
        minutos = (int(self.horaSaida.split(':')[1]) - int(self.horaEntrada.split(':')[1]))
        tempoTotal = horas + minutos
        
        valor_total = (4*f_valor*tempoTotal//60)
        return valor_total - (v_hora/100) * valor_total

    def calculoHoras(self, hora1, hora2):
        horas = 60 * (int(hora2.split(':')[0]) - int(hora1.split(':')[0]))
        minutos = (int(hora2.split(':')[1]) - int(hora1.split(':')[1]))
        tempoTotal = horas + minutos
        return tempoTotal

    def useDiariaNoturna(self, entrada_noturna):
        if (self.horaEntrada == '21:00'):
            return True
        else:
            return False
        
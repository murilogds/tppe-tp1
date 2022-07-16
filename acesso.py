class Acesso:
    horaEntrada = ''
    horaSaida = ''

    def __init__(self, horaEntrada, horaSaida) -> None:
        self.horaEntrada = horaEntrada
        self.horaSaida = horaSaida

    def getPrecoHoraCheia(self):
        horas = 60 * (int(self.horaSaida.split(':')[0]) - int(self.horaEntrada.split(':')[0]))
        minutos = (int(self.horaSaida.split(':')[1]) - int(self.horaEntrada.split(':')[1]))
        tempoTotal = horas + minutos
        if(tempoTotal == 60):
            return 102
        else:
            return 204
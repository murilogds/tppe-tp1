class Acesso:
    horaEntrada = ''
    horaSaida = ''

    def __init__(self, horaEntrada, horaSaida) -> None:
        self.horaEntrada = horaEntrada
        self.horaSaida = horaSaida

    def getPrecoHoraCheia(self):
        return 102
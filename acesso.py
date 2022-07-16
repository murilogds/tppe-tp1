class Acesso:
    horaEntrada = ''
    horaSaida = ''
    tipoEstacionamento = 0

    def __init__(self, horaEntrada, horaSaida, tipoEstacionamento) -> None:
        self.horaEntrada = horaEntrada
        self.horaSaida = horaSaida
        self.tipoEstacionamento = tipoEstacionamento

    def getPrecoHoraCheia(self):
        horas = 60 * (int(self.horaSaida.split(':')[0]) - int(self.horaEntrada.split(':')[0]))
        minutos = (int(self.horaSaida.split(':')[1]) - int(self.horaEntrada.split(':')[1]))
        tempoTotal = horas + minutos
        if(self.tipoEstacionamento == 1):
            f_valor = 30.00
            v_hora = 15
        
        elif(self.tipoEstacionamento == 2):
            f_valor = 20.00
            v_hora = 10
        
        else:
            f_valor = 10.00
            v_hora = 0
        
        valor_total = (4*f_valor*tempoTotal//60)
        return valor_total - (v_hora/100) * valor_total
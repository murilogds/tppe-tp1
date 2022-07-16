class Acesso:
    def __init__(self, horaEntrada = '', horaSaida = '') -> None:
        self.horaEntrada = horaEntrada
        self.horaSaida = horaSaida

    def calculaAcesso(self, estacionamento):
        if self.calculoHoras(self.horaEntrada, self.horaSaida) <= 540:
            if self.calculoHoras(estacionamento.entrada_noturna, self.horaEntrada) < 0:
                return self.getPrecoHoraCheia(estacionamento.valor_fracao, estacionamento.valor_hora)
            else:
                self.getPrecoAcessoNoturno()
        #else:
        #    return diaria diurna

    def getPrecoHoraCheia(self, f_valor, v_hora):
        horas = 60 * (int(self.horaSaida.split(':')[0]) - int(self.horaEntrada.split(':')[0]))
        minutos = (int(self.horaSaida.split(':')[1]) - int(self.horaEntrada.split(':')[1]))
        tempoTotal = horas + minutos
        
        valor_total = (4*f_valor*tempoTotal//60)
        return valor_total - (v_hora/100) * valor_total

    def getPrecoAcessoNoturno(self):
    #     if():
        return 54
    #     else:
    #         return 21

    def calculoHoras(self, hora1, hora2):
        horas = 60 * (int(hora2.split(':')[0]) - int(hora1.split(':')[0]))
        minutos = (int(hora2.split(':')[1]) - int(hora1.split(':')[1]))
        print(hora1)
        print(hora2)
        tempoTotal = horas + minutos
        return tempoTotal
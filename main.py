from acesso import Acesso
from estacionamento import Estacionamento
from exceptions import *
from constants import estacionamento

def verificaEntradaHora(tempo):
    if not tempo: 
        raise DescricaoEmBrancoException('Hora')
    elif tempo.find(':') == -1:
        raise HoraInvalidaException()
    
    horas, minutos = tempo.split(':')

    if not horas.isdigit() or not minutos.isdigit():
        raise HoraInvalidaException()
    elif int(horas) > 23 or int(minutos) > 59:
        raise HoraInvalidaException()

    return tempo



print('Insira a hora de entrada (HH:MM):')
horaEntrada = verificaEntradaHora(input())

print('Insira a hora de saida (HH:MM):')
horaSaida = verificaEntradaHora(input())

print('Insira a placa do carro')
placaCarro = input()

print('É um evento? Digite \'y\' para sim e qualquer coisa para não')
if input() == 'y':
    isEvento = 1
else:
    isEvento = 0

acesso = Acesso(horaEntrada=horaEntrada, horaSaida=horaSaida, isEvento=isEvento, placa=placaCarro)

print(f'O valor do estacionamento é: {acesso.calculaAcesso(estacionamento)}')
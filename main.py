from acesso import Acesso
from estacionamento import Estacionamento
from exceptions import *
from constants import estacionamentoDefault
from utils import verificaEntradaHora, verificaEntradaVazia, verificaValorInvalido

while True:
    print('Insira o valor da fração')
    valor_fracao = verificaValorInvalido(input())
    print('Insira o valor (em %) de desconto da hora cheia')
    valor_hora_cheia =verificaValorInvalido(input())
    print('Insira o valor da diária diurna')
    valor_diaria_diurna = verificaValorInvalido(input())
    print('Insira o valor (porcentagem em relação a diária diurna) da diária noturna ')
    porcentagem_diaria_noturna =verificaValorInvalido(input())
    valor_diaria_noturna = (porcentagem_diaria_noturna/100) * valor_diaria_diurna
    print('Insira o horário mínimo de entrada da diária noturna (HH:MM)')
    entrada_noturna = verificaEntradaHora(input())
    print('Insira o horário máximo de retirada da diária noturna (HH:MM)')
    retirada_noturna = verificaEntradaHora(input())
    print('Insira o valor de acesso mensalista')
    valor_mensalista = verificaValorInvalido(input())
    print('Insira o valor de acesso para eventos')
    valor_evento = verificaValorInvalido(input())
    print('Horário de funcionamento:')
    print('O estacionamento funciona por 24hs? (y/n)')
    isDiaInteiro = input()
    if isDiaInteiro == 'y':
        horario_min_funcionamento = '0:0'
        horario_max_funcionamento = '23:59'
    else:
        print('Insira o horário mínimo de funcionamento: (HH:MM)')
        horario_min_funcionamento = verificaEntradaHora(input())
        print('Insira o horário máximo de funcionamento: (HH:MM)')
        horario_max_funcionamento = verificaEntradaHora(input())
    print('Insira a porcentagem de retorno do contratante')
    valor_contratante = verificaValorInvalido(input())
    print('Insira a capacidade do estacionamento')
    capacidade =verificaValorInvalido(input())
    estacionamento = Estacionamento(
        valor_fracao=valor_fracao,
        valor_hora=valor_hora_cheia,
        diaria_diurna=valor_diaria_diurna,
        diaria_noturna=valor_diaria_noturna,
        entrada_noturna=entrada_noturna,
        retirada_noturna=retirada_noturna,
        valor_mensalista=valor_mensalista,
        valor_evento=valor_evento,
        horario_min_funcionamento=horario_min_funcionamento,
        horario_max_funcionamento=horario_max_funcionamento,
        capacidade=capacidade
    )
    estacionamento = estacionamentoDefault

    retorno_contratante = 0
    print('Quantos acessos foram registrados?')
    acessos = int(input())
    
    for i in range(acessos):
        horaEntrada = ''
        horaSaida = ''
        isEvento = 0
        isMensalista = 0
        print('Insira qual o tipo de acesso:')
        print('1 - Por horário')
        print('2 - Mensalista')
        print('3 - Evento')
        tipo = input()

        if tipo == '1':
            print('Insira a hora de entrada (HH:MM):')
            horaEntrada = verificaEntradaHora(input())

            print('Insira a hora de saida (HH:MM):')
            horaSaida = verificaEntradaHora(input())
        elif tipo == '2':
            isMensalista = 1
        elif tipo == '3':
            isEvento = 1
        else:
            raise ValorInvalidoException()

        print('Insira a placa do carro')
        placaCarro = verificaEntradaVazia(input(), 'Placa')

        acesso = Acesso(horaEntrada=horaEntrada, horaSaida=horaSaida, isEvento=isEvento, placa=placaCarro, isMensalista=isMensalista)

        print(f'O valor do estacionamento é: {acesso.calculaAcesso(estacionamento)} R$')
        retorno_contratante += acesso.getValorContratante(estacionamento)

    print(f'O retorno total do contratante foi de: {retorno_contratante} R$')

    print('Deseja cadastrar um novo estacionamento: (y/n)')
    opcao = input()
    if opcao == 'n':
        break
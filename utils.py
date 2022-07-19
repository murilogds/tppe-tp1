from exceptions import DescricaoEmBrancoException
from exceptions import HoraInvalidaException
from exceptions import ValorInvalidoException

def verificaEntradaVazia(texto, campo):
    if not texto or texto.strip(' ') == '':
        raise DescricaoEmBrancoException(campo)

def verificaEntradaHora(tempo):
    verificaEntradaVazia(tempo, 'Hora')
    if tempo.find(':') == -1:
        raise HoraInvalidaException()
    
    horas, minutos = tempo.split(':')

    if not horas.isdigit() or not minutos.isdigit():
        raise HoraInvalidaException()
    elif int(horas) > 23 or int(minutos) > 59:
        raise HoraInvalidaException()

    return tempo

def verificaValorInvalido(valor):
    if valor.find('.') != -1:
        inteiro, decimal = valor.split('.')
        if not inteiro.isdigit() or not decimal.isdigit():
            raise ValorInvalidoException()
    elif not valor.isdigit():
        raise ValorInvalidoException()

    return float(valor)
        
import pytest
from acesso import Acesso
from estacionamento import Estacionamento

from exceptions import IntervaloInvalidoException


@pytest.mark.parametrize("acesso, estacionamento", [
    (Acesso('23:00', '07:00', 'JHB'), Estacionamento(horario_min_funcionamento='08:00', horario_max_funcionamento='20:00'))])
def testValorInvalidoException(acesso, estacionamento):
    with pytest.raises(IntervaloInvalidoException):
        acesso.calculaAcesso(estacionamento)
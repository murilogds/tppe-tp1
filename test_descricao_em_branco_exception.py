import pytest
from acesso import Acesso

from exceptions import DescricaoEmBrancoException
from utils import verificaEntradaVazia

@pytest.mark.parametrize("horaEntrada,horaSaida,placa", [
    (' ', '08:50', 'BBB-1111'),
    ('08:50', '', 'BBB-1111'),
    ('08:50', '09:50', '')
])
def testeDescricaoEmBrancoExceptionAcesso(horaEntrada, horaSaida, placa):
    with pytest.raises(DescricaoEmBrancoException) as error:
        verificaEntradaVazia(horaEntrada, 'Hora')
        verificaEntradaVazia(horaSaida, 'Hora')
        verificaEntradaVazia(placa, 'Placa')
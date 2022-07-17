import pytest
from acesso import Acesso

from descricao_em_branco_exception import DescricaoEmBrancoException

@pytest.mark.parametrize("horaEntrada,horaSaida,placa", [
    (' ', '08:50', 'BBB-1111'),
    ('08:50', '', 'BBB-1111'),
    ('08:50', '09:50', '')
])
def testeDescricaoEmBrancoExceptionAcesso(horaEntrada, horaSaida, placa):
    with pytest.raises(DescricaoEmBrancoException) as error:
        acesso = Acesso(horaEntrada, horaSaida, placa)
import pytest 
from acesso import Acesso
from estacionamento import Estacionamento

@pytest.mark.parametrize("acesso, estacionamento, saida",[
    (Acesso(placa='AM31J', horaEntrada='03:40', horaSaida='12:40'), Estacionamento(diaria_diurna=30), 30),
])
class TesteFuncionalDiariaDiurna():

    def testeDiariaDiurna(self, acesso, estacionamento, saida):
        assert acesso.calculaAcesso(estacionamento) == saida
import pytest 
from acesso import Acesso
from estacionamento import Estacionamento

@pytest.mark.parametrize("acesso, estacionamento, saida",[
    (Acesso(placa='AM31J', horaEntrada='03:40', horaSaida='12:40'), Estacionamento(diaria_diurna=30), 30),
    (Acesso(placa='AM31J', horaEntrada='10:40', horaSaida='19:55'), Estacionamento(diaria_diurna=50), 50),
    (Acesso(placa='AM31J', horaEntrada='13:10', horaSaida='22:25'), Estacionamento(diaria_diurna=27), 27),
])
class TesteFuncionalDiariaDiurna():

    def testeDiariaDiurna(self, acesso, estacionamento, saida):
        assert acesso.calculaAcesso(estacionamento) == saida
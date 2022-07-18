import pytest 
from acesso import Acesso
from estacionamento import Estacionamento

@pytest.mark.parametrize("acesso, estacionamento, saida",[
    (Acesso(placa='AM31J', horaEntrada='03:40', horaSaida='03:45'), Estacionamento(valor_fracao=30), 30),
    (Acesso(placa='AM31J', horaEntrada='03:40', horaSaida='04:00'), Estacionamento(valor_fracao=50), 100),
    (Acesso(placa='AT31J', horaEntrada='03:40', horaSaida='04:20'), Estacionamento(valor_fracao=20), 60),
])
class TesteFuncionalHoraFracionada():

    def testeHoraFracionada(self, acesso, estacionamento, saida):
        assert acesso.calculaAcesso(estacionamento) == saida
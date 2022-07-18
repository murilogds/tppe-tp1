import pytest 
from acesso import Acesso
from estacionamento import Estacionamento

@pytest.mark.parametrize("acesso, estacionamento, saida",[
    (Acesso(placa='AM31J', horaEntrada='03:40', horaSaida='03:45'), Estacionamento(valor_fracao=30, retornoContratante=0.3), 9),
    (Acesso(placa='AM31J', horaEntrada='03:40', horaSaida='03:45', isEvento=1), Estacionamento(valor_evento=50, retornoContratante=0.2), 10),
])
class TesteFuncionalHoraFracionada():

    def testeHoraFracionada(self, acesso, estacionamento, saida):
        _ = acesso.calculaAcesso(estacionamento)
        assert acesso.getValorContratante(estacionamento) == saida
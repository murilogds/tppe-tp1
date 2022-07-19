import pytest 
from acesso import Acesso
from estacionamento import Estacionamento

@pytest.mark.parametrize("acesso, estacionamento, saida",[
    (Acesso(placa='AM31J', horaEntrada='03:40', horaSaida='03:45'), Estacionamento(valor_fracao=30, retorno_contratante=0.3), 9),
    (Acesso(placa='AM36J', horaEntrada='03:40', horaSaida='03:45', isEvento=1), Estacionamento(valor_evento=50, retorno_contratante=0.2), 10),
    (Acesso('01:00', '03:00', 'ABC123'), Estacionamento(diaria_noturna=20, entrada_noturna='20:00', retirada_noturna='8:00', retorno_contratante=0.5), 10)
])
class TesteFuncionalHoraFracionada():

    def testeHoraFracionada(self, acesso, estacionamento, saida):
        _ = acesso.calculaAcesso(estacionamento)
        assert acesso.getValorContratante(estacionamento) == saida
import pytest 
from acesso import Acesso
from estacionamento import Estacionamento

@pytest.mark.parametrize("acesso, estacionamento, saida",[
    (Acesso('21:00', '23:00', 'ABC123'), Estacionamento(diaria_noturna=54, entrada_noturna='19:00', retirada_noturna='8:00'), 54),
    (Acesso('22:00', '04:00', 'ABC123'), Estacionamento(diaria_noturna=21, entrada_noturna='21:00', retirada_noturna='7:00'), 21),
    (Acesso('01:00', '03:00', 'ABC123'), Estacionamento(diaria_noturna=20, entrada_noturna='20:00', retirada_noturna='8:00'), 20)
])
class TesteFuncionalAcessoNoturno():

    def testeAcessoNoturno(self, acesso, estacionamento, saida):
        assert acesso.calculaAcesso(estacionamento) == saida
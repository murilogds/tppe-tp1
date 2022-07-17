import pytest
from acesso import Acesso
from estacionamento import Estacionamento

@pytest.mark.parametrize("acessos,estacionamento,saidas", [
    (Acesso('8:30', '9:30', 'ABC-1234'), Estacionamento(valor_fracao=30,valor_hora=15), 102),
    (Acesso('9:30', '11:30', 'ABC-1234'), Estacionamento(valor_fracao=30,valor_hora=15), 204),
    (Acesso('8:20', '11:20', 'ABC-1234'), Estacionamento(valor_fracao=20,valor_hora=10), 216),
    (Acesso('12:00', '14:00', 'ABC-1234'), Estacionamento(valor_fracao=10,valor_hora=0), 80)
    ])
class TesteFuncionalAcessoHoraCheia():

    def testAcessoHoraCheia(self, acessos,estacionamento, saidas):
        assert acessos.calculaAcesso(estacionamento) == saidas
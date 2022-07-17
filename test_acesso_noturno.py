import pytest 
from acesso import Acesso
from estacionamento import Estacionamento

class TesteFuncionalAcessoNoturno():
    
    def testeAcessoNoturno1(self):
        acesso = Acesso('21:00', '23:00', 'ABC123')
        estacionamento = Estacionamento(diaria_noturna=54, entrada_noturna='19:00', retirada_noturna='8:00')
        assert acesso.calculaAcesso(estacionamento) == 54
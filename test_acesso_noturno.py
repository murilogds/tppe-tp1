import pytest 
from acesso import Acesso
from estacionamento import Estacionamento

class TesteFuncionalAcessoNoturno():
    
    def testeAcessoNoturno1(self):
        acesso = Acesso('21:00', '23:00', 'ABC123')
        estacionamento = Estacionamento(diaria_noturna=54, entrada_noturna='19:00', retirada_noturna='8:00')
        assert acesso.calculaAcesso(estacionamento) == 54

    def testeAcessoNoturno2(self):
        estacionamento1 = Estacionamento(diaria_noturna=54, entrada_noturna='19:00', retirada_noturna='8:00')
        acesso1 = Acesso('21:00', '23:00', 'ABC123')
        assert acesso1.calculaAcesso(estacionamento1) == 54
        estacionamento2 = Estacionamento(diaria_noturna=21, entrada_noturna='21:00', retirada_noturna='7:00')
        acesso2 = Acesso('22:00', '23:00', 'ABC123')
        assert acesso2.calculaAcesso(estacionamento2) == 21
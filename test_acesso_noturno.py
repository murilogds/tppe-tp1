import pytest 
from acesso import Acesso

class TesteFuncionalAcessoNoturno():
    
    def testeAcessoNoturno1(self):
        acesso = Acesso()
        assert acesso.getPrecoAcessoNoturno() == 54
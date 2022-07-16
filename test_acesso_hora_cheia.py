from acesso import Acesso

class TestAcessoHoraCheia():
    def testAcessoHoraCheiaEstacionamentoUm(self):
        acesso = Acesso('8:30', '9:30')
        assert acesso.getPrecoHoraCheia() == 102
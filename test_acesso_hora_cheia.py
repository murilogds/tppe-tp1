from acesso import Acesso

class TesteFuncionalAcessoHoraCheia():
    def testAcessoHoraCheia1(self):
        acesso = Acesso('8:30', '9:30')
        assert acesso.getPrecoHoraCheia() == 102

    def testAcessoHoraCheia2(self):
        acesso = Acesso('8:30', '9:30')
        assert acesso.getPrecoHoraCheia() == 102
        acesso = Acesso('9:30', '11:30')
        assert acesso.getPrecoHoraCheia() == 204
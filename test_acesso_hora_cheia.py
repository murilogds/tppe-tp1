from acesso import Acesso

class TesteFuncionalAcessoHoraCheia():
    def testAcessoHoraCheia1(self):
        acesso = Acesso('8:30', '9:30', 1)
        assert acesso.getPrecoHoraCheia() == 102

    def testAcessoHoraCheia2(self):
        acesso = Acesso('8:30', '9:30', 1)
        assert acesso.getPrecoHoraCheia() == 102
        acesso = Acesso('9:30', '11:30', 1)
        assert acesso.getPrecoHoraCheia() == 204

    def testAcessoHoraCheia3(self):
        acesso = Acesso('8:20', '11:20', 2)
        assert acesso.getPrecoHoraCheia() == 216
        acesso = Acesso('12:00', '14:00', 3)
        assert acesso.getPrecoHoraCheia() == 80

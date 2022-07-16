import pytest
from acesso import Acesso

@pytest.mark.parametrize("acessos,saidas", [
    (Acesso('8:30', '9:30', 1), 102),
    (Acesso('9:30', '11:30', 1), 204),
    (Acesso('8:20', '11:20', 2), 216),
    (Acesso('12:00', '14:00', 3), 80)
    ])
class TesteFuncionalAcessoHoraCheia():
    def testAcessoHoraCheia(self, acessos, saidas):
        assert acessos.getPrecoHoraCheia() == saidas
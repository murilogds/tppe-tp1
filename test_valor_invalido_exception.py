import pytest

from exceptions import ValorInvalidoException
from utils import verificaValorInvalido


@pytest.mark.parametrize("input", ['', '-78', '-5.99', '7,88', '3.A'])
def testValorInvalidoException(input):
    with pytest.raises(ValorInvalidoException):
        verificaValorInvalido(input)
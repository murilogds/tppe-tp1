class DescricaoEmBrancoException(Exception):

    def __init__(self, campo: str, *args: object) -> None:
        super().__init__(*args)
        self.campo = campo

    def __str__(self) -> str:
        return f'O campo {self.campo} não pode receber uma descrição em branco'

class HoraInvalidaException(Exception):

    def __init__(self, *args: object) -> None:
        super().__init__(*args)

    def __str__(self) -> str:
        return '''
            O formato da hora está inválido, deve ser no formato 
            HH:MM sendo HH valores de 0 a 23 e MM valores de 0 a 59
        '''

class ValorInvalidoException(Exception):

    def __init__(self, *args: object) -> None:
        super().__init__(*args)

    def __str__(self) -> str:
        return '''
            O valor digitado é inválido digite um número positivo 
            usando . como separador (Ex.: 5.50)
        '''

class IntervaloInvalidoException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

    def __str__(self) -> str:
        return '''
            O intervalo informado não está dentro do horário de
            funcionamento do estacionamento
        '''
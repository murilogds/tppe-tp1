class DescricaoEmBrancoException(Exception):

    def __init__(self, campo: str, *args: object) -> None:
        super().__init__(*args)
        self.campo = campo

    def __str__(self) -> str:
        return f'O campo {self.campo} não pode receber uma descrição em branco'

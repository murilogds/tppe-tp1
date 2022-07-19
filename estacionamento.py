class Estacionamento:
    def __init__(
        self,
        valor_fracao = 0,
        retorno_contratante = 0,
        valor_hora = 0,
        diaria_diurna = 0,
        diaria_noturna = 0, 
        entrada_noturna = '23:59',
        retirada_noturna = '00:00',
        valor_mensalista = 0,
        valor_evento = 0,
        horario_min_funcionamento = '00:00',
        horario_max_funcionamento = '23:59',
        capacidade = 0,
        acessos = []
    ):
        self.valor_fracao = valor_fracao
        self.retorno_contratante = retorno_contratante
        self.valor_hora = valor_hora
        self.diaria_diurna = diaria_diurna
        self.diaria_noturna = diaria_noturna
        self.entrada_noturna = entrada_noturna
        self.retirada_noturna = retirada_noturna
        self.valor_mensalista = valor_mensalista
        self.valor_evento = valor_evento
        self.horario_min_funcionamento = horario_min_funcionamento
        self.horario_max_funcionamento = horario_max_funcionamento
        self.capacidade = capacidade
        self.acessos = acessos

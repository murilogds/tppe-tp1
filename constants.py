from estacionamento import Estacionamento

estacionamentoDefault = Estacionamento(
    valor_fracao = 30,
    retorno_contratante = 0.5,
    valor_hora = 15,
    diaria_diurna = 120,
    diaria_noturna = 54, 
    entrada_noturna = '19:00',
    retirada_noturna = '08:00',
    valor_mensalista = 600,
    valor_evento = 50,
    horario_min_funcionamento = '6:00',
    horario_max_funcionamento = '22:00',
    capacidade = 300,
    acessos = []
)
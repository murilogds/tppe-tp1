# Simplicidade

## Descrição

Desenvolver códigos simples de serem lidos e interpretados. Essa característica é importante porque facilita na manutenção do código. Se o código for muito complexo, outros programadores não entenderão o que aquele código está fazendo, isso fará que percam tempo interpretando a função daquele código no projeto o que prejudica a equipe ou a empresa que trabalha naquele projeto.

Portanto a simplicidade é importante porque além de estar se comunicando com a máquina, o programador também vai estar se comunicando com futuros programadores e participantes daquele projeto.

## Relação com maus cheiros

Os seguintes maus cheiros estão relacionados com essa característica:

- Método longo: métodos longos são muito grandes, o que os tornam difíceis de entender;
- Classes grandes: Caem na mesma questão dos métodos longos, também pode ser um sinal de repetições no código;
- Longa lista de parâmetros: Trazem inconsistência, se tornam difíceis de entender e portanto difíceis de utilizar
- Aglomerados de dados: Apesar de aparecerem juntos com frequência, dados aglomerados não estão em conjunto em uma classe, isso pode gerar a sensação de bagunça ao código;
- Cadeias de mensagens: Quando há um loop de métodos que chamam outros métodos, isso também é um sinal de que o código não está simples.

## Operações de refatoração relacionadas

As seguintes refatorações podem ser aplicadas:

- Extrair método: Tranformar em um método separado pode auxiliar com métodos longos, diminuindo assim seu tamanho. Maus cheiros relacionados: Método longo, cadeias de mensagens;
- Extrair classe/subclasse: Serve para agrupar um número de variáveis que juntas vão fazer algum sentido como uma subclasse da classe em questão ou para o projeto em si. Maus cheiros relacionados: Classe grande, aglomerado de dados
- Substituir parâmetro por método: Ao invés de passar o dado como parâmetro, realizar a chamada de um método do objeto que possua o dado vai diminuir a quantidade de parâmetros passados. Maus cheiros relacionados: longa lista de parâmetros.

Exemplo de refatoração no código de levou a ter a característica em análise:

![](./assets/simplicidade.png)

A imagem acima demonstra um exemplo de método extraído que ajuda a compreender o que o código está buscando fazer, tornando assim ele mais simples de ser compreendido.

## Bibliografia

https://programadorviking.com.br/qualidade-de-software-descubra-tudo-que-o-seu-codigo-deve-ter/#Simplicidade
# Elegância

## Definição

Apenas um código eficiente não é suficiente em projetos reais já que, se for considerar apenas a eficiência do código, apesar de um compilador rodá-lo e aceitá-lo como funcional, ao longo do tempo se torna difícil de realizar a sua manutenção.

Por volta de 50% do esforço da manutenção é entender o software a ser modificado (PARIKH; ZVENGINTZOC, 1983 apud PFLEEGER; ATLEE, 2009, p. 546). É perceptível que a elegância, assim como a simplicidade é de extrema importância para uma futura manutenção no código já que um bom código precisa ser facilmente entendido por outro desenvolvedor.

Escrever um código elegante pode ser comparado como escrever um livro. A escrita é feita para que o leitor possa entender da forma mais clara possível a ideia que está sendo repassada. Como um livro, um código limpo proporciona uma leitura natural a um programador, expondo as questões do problema a ser solucionado.

## Relação com maus cheiros

- Código duplicado: Duplicação de código que poderia ser uma função é um mau cheiro que tira a elegância do código e dificulta na leitura;
- Método longo: Métodos longos são cansativos, portanto perde a característica de uma leitura natural ao programador;
- Longa lista de parâmetros: Trazem inconsistência, se tornam difíceis de entender e portanto difíceis de utilizar;
- Classe grande: Classes grandes têm o mesmo problema de métodos longos, portanto também tornam a leitura cansativa;
- Mudanças divergentes: Quando se precisa fazer diversas alterações em uma classe ao fazer uma mudança, é aumentada a complexidade, por consequência não é facil de outro desenvolvedor entender o funcionamento do código;
- Aglomerados de dados: Aglomerados de dados parecem poluição de código, assim perde-se a elegância do código ao poluí-lo;
- Cadeias de mensagens: Assim como em mudanças divergentes, casos de cadeias de mensagens tornam difícil a compreensão do código.


## Operações de refatoração relacionadas

- Extrair método: Tranformar em um método separado pode auxiliar com métodos longos, diminuindo assim seu tamanho, também pode acomodar os elementos de variação em um único lugar. Maus cheiros relacionados: Método longo, cadeias de mensagens, mudanças divergentes;
- Extrair classe/subclasse: Serve para agrupar um número de variáveis que juntas vão fazer algum sentido como uma subclasse da classe em questão ou para o projeto em si. Maus cheiros relacionados: Classe grande, aglomerado de dados
- Substituir parâmetro por método: Ao invés de passar o dado como parâmetro, realizar a chamada de um método do objeto que possua o dado vai diminuir a quantidade de parâmetros passados. Maus cheiros relacionados: longa lista de parâmetros.

Exemplo de refatoração no código que levou a ter a característica em análise:

![](./assets/simplicidade.png)

Exemplo aplicado também em simplicidade, é possível perceber um código extraído para o cálculo de horas, por conta desta extração o código se torna mais elegante e fácil de ser lido.

## Bibliografia

Qualidade de código, Fábio Levy Siqueira, 27/03/2018
https://www.devmedia.com.br/qualidade-no-codigo-java-com-boas-praticas-e-clean-code/39472
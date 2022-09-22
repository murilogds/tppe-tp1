# Ausência de Duplicidade

## Descrição

É ideal que em um projeto de software, não exista nenhuma duplicação de código, visto que quando há duplicação, o código perde em simplicidade e elegância. Quando há dois trechos similares de códigos, é comum a situação em que um bug é corrigido em um trecho, mas não no outro, causando assim uma inconsistência no código.

Esse princípio é muito reforçado pelo padrão de desenvolvimento DRY(Don't Repeat Yourself) que consiste em transformar trechos de códigos duplicados e repetidos dentro do código em funções.

## Relação com maus cheiros

- Código duplicado: Qualquer trecho de código repetido mais de uma vez indica que o código contem duplicidade.

## Operações de refatoração relacionadas

- Extrair método: Transformar um trecho que tá duplicado em um método da classe;
- Método template: Extrair comportamento comum de dois métodos e implementar a variabilidade em subclasses.

Exemplo de refatoração no código que levou a ter a característica em análise:

![](./assets/simplicidade.png)

Exemplo também aplicado em simplicidade, antes dessa refatoração o método calculoHoras tinha sua lógica repetida em vários trechos do código, com a extração dessa lógica para o método calculoHoras, foi possível diminuir a duplicidade do código.
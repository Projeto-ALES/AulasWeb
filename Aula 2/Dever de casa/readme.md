# Dever de Casa

Pronto(a) pra colocar em prática todo esse conhecimento em Python? Eu também!

Abaixo estão alguns probleminhas que vocês já são capazes de resolver. Ao lado do nome deles vocês vão encontrar algumas `*`, sendo que `*` significa que é um problema fácil e `*****` que o programa é difícil

## Vários números! `*`

Considere dois números, 10 e 2.
Faça um programa que imprime a a soma, subtração, divisão, multiplicação, resto da divisão e potência deles.

#### Dicas:
- Leia as operações matemáticas nas notas de aula!

#### Exemplo de saída:
```
12
8
5
20
0
100
```

## Centenários `**`

Faça um programa que recebe o nome de um usuário e a idade dele. Seu programa deve, então, imprimir na tela usando o `print` uma mensagem direcionada ao usuário(usando o nome dele) e dizendo o ano(considerando que estamos em 2017) que ele ou ela vai completar 100 anos de idade.

#### Dicas:
- Se não souber como receber informação do usuário, leia a penúltima seção das anotações de aula!
- Você pode converter _texto_(_strings_) para _números inteiros_(_int_) usando `int()`!
- Você pode converter _números inteiros_(_int_) para _texto_(_strings_) usando `str()`!
- Se você tiver recebendo erros do tipo `TypeError: unsupported operand type(s) for +`... provavelmente é porque você está somando uma _string_ com um _int_. Use as dicas acima pra converter entre eles!

#### Exemplo de entrada:
```
>>> Qual seu nome? Rodolfo
>>> Qual sua idade? 41
```
#### Exemplo de saída:
```
Rodolfo, você vai fazer 100 anos em 2076!
```

## Par ou Ímpar! `**`

Faça um programa que recebe um número e responde dizendo se é par ou ímpar.

#### Dicas:
- Se não souber como receber informação do usuário, leia a penúltima seção das anotações de aula!
- Você pode converter _texto_(_strings_) para _números inteiros_(_int_) usando `int()`!
- Existe uma operação matemática que torna isso de ser par ou ímpar bem simples! Leia as anotações de aula!
- Lembre-se de condicionais!

#### Exemplo de entrada:
```
>>> Digite um número: 42
```
#### Exemplo de saída:
```
É par!
```

## Só para menores! `***`

Faça um programa que recebe um número do usuário e imprime todos os valores de uma lista que são _menores que_ o valor recebido.

Use a lista `[10, 20, 25, 17, 21, 16, 8, 42, 18, 14, 12, 50, 5, 2]`

#### Dicas:
- Condicionais, loops e `input`, temos de tudo!
- Não esqueça de colocar os **espaços** de indentação no seu código!

#### Exemplo de entrada:
```
>>> Digite um número: 12
```
#### Exemplo de saída:
```
10
8
5
2
```

## Divisores! `***`

Faça um programa que recebe um número do usuário e imprime todos os números que são divisores desse número!

**OBS**: Divisor é um número que, ao dividir outro, tem _resto_ igual a zero.

Ex: 2 é divisor de 10, mas 3 não é divisor de 10.

#### Dicas:
- Condicionais, loops e `input`, temos de tudo!
- Não esqueça de colocar os **espaços** de indentação no seu código!
- Lembre-se: Um divisor **não** pode ser maior que o número que está tentando dividir

#### Exemplo de entrada:
```
>>> Digite um número: 16
```
#### Exemplo de saída:
```
1
2
4
8
16
```

## Pedra, Papel e Tesoura! `****`

Faça um jogo de pedra, papel e tesoura para dois jogadores!

Seu jogo deve receber a jogada de um jogador, receber o do outro e falar qual deles venceu. Depois disso ele tem que perguntar se os jogadores querem continuar jogando. Se eles disserem que sim, continue o jogo. Se disserem que não, termine.

**Lembre-se**: Tesoura perde de pedra. Pedra perde de papel. Papel perde de tesoura.

#### Dicas:
- Condicionais, loops e `input`, temos de tudo!
- Não esqueça de colocar os **espaços** de indentação no seu código!
- Seu jogo tem que ser _infinito_. Que tal um _loop infinito_ pra solucionar isso?

#### Exemplo de execução:
```
>>> Jogador 1: Pedra
>>> Jogador 2: Papel
Jogador 2 venceu!
>>> Jogar novamente? Sim
>>> Jogador 1: Tesoura
>>> Jogador 2: Tesoura
Empate!
>>> Jogar novamente? Não
Fim de jogo!
```

#### Bônus!
E se o jogador digitar `sim` ao invés de `Sim`, ou digitar `SIM`? Existe uma forma de considerar todos os casos de uma vez?
- Dica: A diferença entre essas entradas é elas serem _maiúsculas_ ou _minúsculas_!


## Invertendo as coisas! `*****`

Faça um programa (usando funções!) que recebe uma _string_ e inverte a posição das palavras(mas não as palavras em si)

#### Dicas:
- Que tal começar _dividindo_ a string em palavras?
- Pra resolver esse problema você tem que estar no nível de _cortar avançado_!

#### Exemplo de entrada:
```
>>> Digite uma string: Meu nome é Bob
```
#### Exemplo de saída:
```
Bob é nome Meu
```

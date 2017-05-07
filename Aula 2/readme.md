# Aula 2

Nessa aula nós revisitamos todo o básico de Python, para finalizar a introdução à linguagem

# Python, de 0 a 100

### Iniciando o interpretador de python
Python é uma linguagem interpretada e, por isso, podemos executar código usando o interpretador.

Para fazer isso em um computador que já tem python instalado(como o do Cloud9), acesse o terminal e execute:
```
python
```
A partir daí tudo que você escrever será interpretado como código python.

```
$ python
Python 3.5.2 |Anaconda custom (x86_64)| (default, Jul  2 2016, 17:52:12)
[GCC 4.2.1 Compatible Apple LLVM 4.2 (clang-425.0.28)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

Experimente escrever algo como `1 + 1` e ver o que acontece

Tudo que está nesse tutorial você pode testar usando isso aí.

Pra fechar, basta digitar `exit()`

## Olá, Mundo
A coisa mais básica que podemos fazer é imprimir na tela.

Fazemos isso usando a função `print`. Por exemplo:

```
print("Olá, mundo!")
```

## Regras de Python
Python, como qualquer outra linguagem, tem algumas regrinhas que devemos seguir
#### Indentação
Python, ao contrário de outras linguagens como C ou Java, define seus _escopos_ usando indentação, não caracteres especiais.

Isso significa que enquanto em C ou Java você escreveria o seguinte pra definir uma condicional:
```C
if (numero > 5) {
    printf("numero é maior que 5");
}
else {
    printf("numero é menor ou igual a 5");
}
```
Em python, você não usa os `{ }`, mas adiciona `:` ao final de cada entrada de escopo e coloca _espaços_ no começo do bloco de texto que deve estar em um escopo diferente:
```Python
if numero > 5:
    print("numero é maior que 5")
else:
    print("numero é menor ou igual a 5")
```
Geralmente se usa 4 espaços, mas você pode usar quantos quiser, desde que você seja **consistente**.

Lembrando que `if` significa "se" em português e `else` significa "senão"

#### Pontos e vígulas
Como você pode ter percebido no exemplo acima, em Python não utilizamos `;` para terminar uma linha, como fazemos em C e Java.
#### Declaração de variáveis
Python é uma linguagem de [tipagem dinâmica](https://pt.wikipedia.org/wiki/Sistema_de_tipos), ou seja, você, programador(a), não precisa dizer pro Python _o que é_ alguma coisa. Python vai decidir isso por você de acordo com o contexto.

Enquanto que em C e Java você faria o seguinte pra definir um número inteiro e um texto:
```C
int i = 5;
char texto[] = "Olá, mundo!"
```

Em python, basta:
```Python
i = 5
texto = "Olá, mundo!"
```

Observe que para atribuir um valor a uma variável, sempre usaremos o formato:
```Python
variavel = valor
```

## Tipos de variáveis em Python
Apesar de você não ter que _declarar_ os tipos das suas variáveis, eles ainda existem.

Textos não são números e números inteiros não são frações.

#### Números inteiros
São, bem como o nome diz, números inteiros, como 4, 5, -3

Criamos variáveis inteiras usando esses números, como em
```Python
numero1 = 5
numero2 = 42
i = 10
```
#### Pontos flutuantes
São nomes chiques pra frações.

Criamos pontos flutuantes ao criar números com vírgulas
```Python
pf1 = 4.2
pf2 = 534.234
k = 0.435283
```
#### Texto (Strings)
Textos em python, chamados de _Strings_, são criados usando àspas em volta de um texto.
As àspas podem ser duplas(`"`) ou simples(`'`), desde que você comece e termine com o mesmo tipo:
```Python
texto1 = "Olá, Mundo!"
texto2 = 'Como vai?'
t = 'Textos com "" àspas difentes dentro são válidos'
```

### Estruturas de dados
Python já vem com algumas estruturas de dados úteis
#### Listas
São basicamente isso. Coisas em uma lista.

Para criar uma lista vazia, fazemos:
```Python
uma_lista = []
```

Podemos adicionar elementos à lista usando o método `.append()`
```Python
uma_lista = []
uma_lista.append("Um texto")
y = 5
uma_lista.append(y)
```
Podemos criar a lista já com elementos, separando eles com vírgulas:
```Python
uma_lista = ["Outro texto", 42, 10.5]
```

E nós podemos acessar elementos de uma lista fornecendo o _índice_ que queremos acessar

**OBS:** Em python nós usamos o índice `0` para acessar o primeiro elemento das coisas
```Python
>>> uma_lista[0]
"Outro texto"
>>> uma_lista[2]
10.5
```

Observe que nós não podemos acessar elementos que não existem. O código abaixo geraria um erro, já que estaríamos acessando algo que não existe na lista:
```Python
uma_lista = ["Outro texto", 42, 10.5]
print(uma_lista[20])
```

#### Outras estruturas
Python tem várias outras estruturas úteis que não vamos falar aqui. Caso tenha interesse:
- [Python datastructures em Português](http://turing.com.br/pydoc/2.7/tutorial/datastructures.html)

## Operações
Python nos permite executar diversas operações em nossos dados. A mais básica é a soma:

```Python
x = 1
y = 2
z = x + y
```
#### Operações comuns
Também podemos fazer outras operações matemáticas que já conhecemos da escola:
```Python
numero = 1 + 2 * 10 / 4
```
Observe que a _sequência_ das operações em Python é a mesma que na matemática normal.

Começamos pelas multiplicações e divisões e só então fazemos as somas, logo o resultado da equação acima é `6`

#### Módulo
Módulo, em programação, é uma operação que nos fornece o **resto da divisão de dois números** e é representado pelo símbolo `%`
```Python
resto = 10 % 4
```
Nos dará `2`, pois a divisão de 10 por 4 é 2 com 2 de resto.

Isso é útil para saber se um número é divisível por outro e para saber se um número é par ou ímpar:
```Python
10 % 2
```
Terá resultado `0`, pois 10 é divisível por 2 (logo 10 é par)
```Python
11 % 2
```
Terá resultado `1`, pois 11 não é divisível por 2, logo 11 é ímpar.

Também podemos verificar se um número é divisível por qualquer outro. Ex:
```Python
39 % 3
```
Terá resultado `0`, pois 39 é divisível por 3

#### Potência
Para elevar um número a uma potência, usamos `**`
```Python
3 ** 2
```
Terá resultado 9, pois é 3 ao quadrado.

#### Operações com outras coisas
Números não são as únicas coisas que podemos manipular. Também podemos somar coisas como textos:

```Python
texto = "Olá," + " " + "mundo!"
```

E multiplicar também:
```Python
textos = "Olá " * 10
```

Podemos fazer operações assim com listas também:
```Python
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista3 = lista1 + lista2
lista4 = lista1 * 10
```

## Operações especiais
Além das operações acima, temos algumas que são bem especiais
#### Tamanho de um texto ou lista

Podemos verificar o número de elementos em uma lista ou o tamanho de um texto usando a operação `len()`, onde 'len' vem de 'length', que significa 'tamanho' ou 'comprimento' em inglês.

```Python
frase = "Eu sou um texto"
len(frase)
```
Nos retorna o tamanho do texto.

Podemos fazer com listas também:
```Python
lista = [1, 2, 50, 10, 23, 42]
len(lista)
```
Deve retornar `6`, pois a lista tem 6 elementos

#### Posição de algo em uma lista ou texto
Como visto, podemos encontrar o elemento em uma posição qualquer em um texto ou lista usando o `[i]`
```Python
texto = "Um texto"
texto[5]
```
Pega o _sexto_ elemento (letra) no texto

Podemos também pegar onde _algo específico está_, usando o `.index()`
```Python
texto = "Um texto aqui"
texto.index("aqui")
```
Vai nos dizer onde `aqui` está no texto.

Podemos fazer o mesmo com listas:
```Python
lista = [1, 2, 50, 10, 23, 42]
lista.index(50)
```
Vai retornar `2`, pois o `50` está na terceira posição (**OBS**, lembre-se que nós sempre começamos a contar do **0**, não do **1** em programação)

#### Número de vezes que algo se repete
Também podemos contar o número de repetições de algo em um texto ou lista usando `.count()`
```Python
texto = "Eu sou um texto"
texto.count("u")
```
Vai retornar 3, pois `u` ocorre 3 vezes no texto.

Podemos fazer o mesmo com listas

#### Cortar textos e listas
Nós podemos cortar pedaços do texto ou lista usando `[:]`, onde o espaço antes do `:` indica onde o corte começa (vazio sendo no começo do texto ou lista), e o espaço depois do `:` indica onde o corte termina (vazio sendo o final do texto ou lista)

```Python
texto = "Eu sou um texto"
texto[:]
```
Nos retorna o texto inteiro, pois vai do começo ao fim nos cortes

```Python
texto = "Eu sou um texto"
texto[7:13]
```
Vai retornar `'um tex'`, pois começamos o corte no oitavo elemento e vamos até o décimo segundo.

```Python
texto = "Eu sou um texto"
texto[7:]
```
Vai retornar `'um texto'`, pois vai do oitavo até o final

Nós também podemos acessar índices negativos, que dão a volta na lista ou texto:
```Python
texto = "Eu sou um texto"
texto[-1]
texto[-2]
```
Vai retornar `'o'` e `'t'`, pois é o último e o penúltimo, respectivamente, elementos na lista ou texto.

#### Cortar avançado
Outra coisa que você pode fazer é alterar o _passo_ que você salta os elementos da lista.

Por exemplo, dada a lista `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]`, podemos selecionar _apenas_ os elementos pares entre o segundo e o oitavo elemento da seguinte forma:
```Python
>>> lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> lista[2:8:2]
[2, 4, 6]
```

Esse formato: `lista[2:8:2]` é levemente diferente do que vimos ali em cima. Ele adiciona um `:` a mais, e esse `:` define o _passo_, ou seja, quantos elementos nós pulamos entre cada selecionado. No caso `lista[2:8:2]`, nós vamos do segundo elemento, o `2` na lista, até o oitavo elemento, o `8` na lista(não incluso), saltando um a cada elemento por causa do passo `2`. Ou seja, saltamos os números ímpares.

Podemos fazer o mesmo para os números pares:
```Python
>>> lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> lista[1:8:2]
[1, 3, 5, 7]
```

E podemos, claro, usar outros saltos (3, por exemplo):
```Python
>>> lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> lista[1:8:3]
[1, 4, 7]
```

Podemos também usar saltos negativos! Esses são interessantes, pois essencialmente nos permitem percorrer a lista ao contrário!
```Python
>>> lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> lista[::-1]
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
```

Nesse caso de cima nós percorremos a lista inteira(`[:]`) com o salto sendo `-1`, ou seja, não saltando nada, mas indo ao contrário na lista. Wow!

#### Maiúsculas e minúsculas.
Podemos fazer com que todas as letras de um texto fiquem maiúsculas:
```Python
texto = "Eu sou um texto"
texto.upper()
```

e minúsculas:
```Python
texto = "Eu sou um texto"
texto.lower()
```

#### Dividir o texto
Podemos dividir nosso texto em vários pedaços usando `.split()`

Por exemplo, vamos separar todas as palavras do texto (ou seja, separar nos espaços entre as palavras)

```Python
texto = "Eu sou um texto"
texto.split(" ")
```
Observe que existe um espaço entre as àspas do `split`. Isso vai nos retornar uma lista contendo as palavras. Nesse caso, teremos uma lista:
```Python
['Eu', 'sou', 'um', 'texto']
```

## Condições
Em Python temos diversas formas de testar condições.

Condições são interessantes porque elas sempre são ou **verdadeiras** (`True`) ou **falsas** (`False`)

#### Igualdade

Podemos testar se um elemento equivale a outro usando `==` (observe que são dois `=`, que é difernte do que vimos na hora de definir uma variável)

```Python
x = 1

x == 2
x == 1
```
Vamos ter `False` no primeiro e `True` no segundo.

Também podemos fazer outras operações, como:
- `>` maior que
- `<` menor que
- `>=` maior ou igual
- `<=` menor ou igual
- `==` igual a
- `!=` diferente de

#### Lógica

Podemos usar as operações acima e lógica pra criar operações mais complexas.

Por exemplo, podemos checar se dois valores são **ambos** verdadeiros usando o `and`
```Python

x = 1
y = 2

x > 0 and y < 10
```
Vai ser `True`, já que ambos são verdadeiro. Isso retornará `False` em qualquer outro caso.

Temos também o `or`, que verifica se **pelo menos um** dos valores é verdadeiro:
```Python
x = 1
y = 15

x > 0 or y < 10
```
Vai ser `True`, pois mesmo que o segundo seja `False`, temos o primeiro sendo verdadeiro. Isso só será `False` caso ambos sejam falsos.

#### Outras condições

Outra condição útil que podemos usar é o **pertencimento**, usando o `in`, ou seja, podemos testar pra ver se um elemento está dentro de outro. Isso é útil com listas:
```Python
palavra = "mundo"
texto = "Olá, mundo!"

palavra in mundo
```
Será `True`, pois palavra está em texto.

Podemos fazer isso para listas também:
```Python
numero = 30
lista = [1, 2, 40, 50]

numero in lista
```
Será `False`, pois `30` não está na lista


#### Testando condições
O principal uso dessas coisas que vimos acima é pra testarmos e executarmos códigos com base em respostas condicionais. O maior exemplo disso é o `if`.

O `if` só executa o código que está dentro dele caso sua condição seja `True`.

Podemos adiconar `elif` e `else` ao `if` para executar outros códigos caso a condição seja `False`

Exemplo:
```Python
x = 10

if x < 5:
    print("x menor que 5")
elif x == 8:
    print("x é 8")
else:
    print("x é outra coisa")
```

Como `x` não é menor que 5 e nem é 8, cairemos no último caso e imprimiremos `"x é outra coisa"`

## Loops
Às vezes nós queremos executar algo várias vezes seguidas. Pra isso servem loops, ou repetições.

#### For Loops
As mais simples são `for` loops:
```Python
for numero in [1, 2, 3, 10, 20, 30]:
    print(numero)
```
Vai fazer o que o texto implica: Vai executar o `print(numero)` para cada `numero` dentro de `[1, 2, 3, 10, 20, 30]`.

Podemos fazer o mesmo com textos:
```Python
for letra in "Sou um texto":
    print(letra)
```
Onde `letra` será cada letra dentro de `"Sou um texto"`

#### range()
O range é especial porque permite que criemos listas inteiras de números facilmente. Isso é útil quando queremos um loop que execute várias vezes

```Python
for numero in range(10):
    print(numero)
```
Vai executar o `print`, com o `numero` sendo cada valor entre 0 e 9, já que temos o `range(10)`.

#### While Loops
Outro tipo de loops útil é o `while`.

Ele permite que executemos o código dentro dele **enquanto** sua condição for verdadeira:
```Python
numero = 0
while numero < 5:
    numero = numero + 1
    print(numero)
```
Onde vamos adicionar 1 ao `numero` a cada iteração do loop, terminando quando `numero` for 5.

#### Loops infinitos
Podemos usar o `while` pra criar um loop infinito definindo uma condição que vai ser verdadeira pra sempre:
```Python
numero = 0
while True:
    numero += 1
    print(numero)
    if numero > 5:
        break
```
Nesse código, o loop é infinito pois sua condição é `True`, que sempre é verdadeira, então adicionamos um ao `numero` a cada iteração (**OBS**: `numero += 1` equivale a `numero = numero + 1`) e então, caso `numero` seja maior que 5, nós damos um `break`, que é um comando especial que interrompe imediatamente aquele loop.

## Funções
Quando nós usamos o `print()`, estamos, de fato, **chamando** a função chamada `print` e usando o parâmetro que queremos imprimir na tela.

Vamos aprender agora a criar nossas próprias funções.

#### Definindo funções
Para definir uma função, devemos usar o comando `def`, seguido do nome da nossa função e os argumentos que ela vai receber:
```Python
def minha_funcao():
    print("Eu sou uma função")
```

Podemos então chamar essa função em outra parte do código, ou até em loops:
```Python
for numero in range(10):
    minha_funcao()
```
Nesse caso vamos chamar nossa função 10 vezes

Mas essa função é bem simples. Ela apenas imprime um texto na tela. Vamos fazer algo mais interessante:

#### Parâmetros e retorno
Como em `print()`, pode ser interessante dizer algo pra nossa função e deixar ela usar aquilo pra fazer alguma coisa. Pra isso servem os parâmetros.

Da mesma forma, podemos querer que nossa função **retorne** alguma coisa de dentro dela. Por exemplo, podemos fazer uma função que pega dois números, calcula a soma deles e retorna a soma:
```Python
def soma_numeros(a, b):
    c = a + b
    return c
```

Nesse caso, nossa função recebe dois parâmetros(`a` e `b`), ou argumentos, salva a soma em `c` e retorna `return` o valor de `c`

Podemos, então, usar isso em um loop:
```Python
for numero in range(10):
    print(soma_numeros(numero, numero * 2))
```
Isso pode parecer um pouco complicado, mas se você parar pra pensar e conseguir entender o que está acontecendo aí, vai valer muito à pena.

# Escrevendo programas em Python
Você já sabe como executar comandos usando o interpretador, mas e se você quiser fazer um programa maior?

É simples!

Se você estiver usando o Clou9, basta clicar lá em cima em `File` (que significa arquivo), depois clicar em `New File`

Agora basta escrever seus códigos no arquivo novo que vai abrir.

Quando terminar de escrever, clique em `File` novamente e clique em `Save`. Escolha um nome pro seu arquivo. Pode ser qualquer coisa, mas no final do nome tem que ter um `.py`

Logo, se você decidir criar um arquivo chamado `programa`, deve escrever `programa.py`

Com seu programa salvo, vá no terminal que fica logo em baixo da janela do arquivo, onde você estava usando o interpretador de Python antes, e digitar
```
python programa.py
```
Substituindo `programa.py` pelo nome do seu programa.

Isso vai executar ele!

**Lembre-se**: Sempre que você alterar o seu programa, não esqueça de salvar ele! Se você não salvar, suas alterações não vão ser consideradas quando você executar seu programa

## Lendo entradas
Às vezes, especialmente quando executamos programas maiores, é bacana poder digitar os valores que queremos, ao invés de ter que colocar tudo no código.

Por exemplo, digamos que você quer fazer um programa que lê o seu nome e diz "Olá, <seu nome>".

Como ler esse nome? Você pode usar uma função chamada `input()`, que significa "entrada", ou coisa que você insere no programa.

O `input()` sempre considera tudo que ele lê como sendo texto, ou seja, `string`. Pra esse caso, então, não tem problema, mas vamos ver uns casos que talvez tenha. Pra esse caso, nós faríamos:

```Python
nome = input("Digite seu nome: ")

print(nome + ", como vai você?")
```

O argumento que o `input` recebe é o texto que vai aparecer quando ele te pedir pra digitar seu nome. É só um texto pra deixar bonitinho.

Aquela nossa soma no `print(nome + ", como vai você?")` só funciona porque tanto o `nome` quanto `", como vai você?"` são strings. Como vimos antes, soma de strings é permitido, mas não de strings com números.

Mas então, como nós podemos fazer pra ler um número? Digamos que a gente quer fazer um programa pra calcular a soma de dois números.

Uma primeira ideia poderia ser fazer o seguinte:
```Python
a = input("Primeiro número: ")
b = input("Segundo número: ")

print(a + b)
```
**Mas isso vai dar errado!** Não necessariamente porque vai dar erro, mas porque não vai fazer o que a gente quer. Digamos que você digite `10` e `30`. O que você espera ver na resposta é `40`, mas o que você vai ter é `1030`, pois o `input` entendeu que você digitou uma _string_ `10` e outra `30`, não um _número inteiro_, como você queria.

Pra corrigir isso, basta você dar a certeza pro Python que o que você vai digitar é um número inteiro. Pra isso nós usamos o `int()` e envolvemos o `input` com ele:
```Python
a = int(input("Primeiro número: "))
b = int(input("Segundo número: "))

print(a + b)
```
Assim a gente garante que o `a` e `b` serão _números inteiros_, não _strings_ e tudo vai dar certo como nós esperávamos.

# Coisas do futuro
Daqui pra frente não vamos mais revisar essas coisas de python. Vou assumir que você já estudou tudo isso em casa e nós vamos começar a trabalhar em coisas mais interessantes daqui pra frente.

Por isso, peço que se dedique a estudar um pouco e a fazer a lição de casa, pra que tudo isso esteja claro em sua mente quando chegar nossa próxima aula

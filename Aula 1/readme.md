# Aula 1

Nessa aula nós vimos a diferença entre Scratch e Python, aprendendo como fazer cada uma das coisas que fazíamos em Scratch, em Python.

Nós também aprendemos a mexer no Cloud9 e começamos a fazer nossos primeiros programas.

## Scratch vs. Python

### Funções

Lembrem-se que em Scratch, para rodar nossos programas, nós precisávmos clicar naquela bandeira verde.

Em nosso primeiro programa de Scratch, nós fazíamos com que o gatinho dissesse "Olá, mundo!" na tela. Para fazer a mesma coisa em Python, apesar de não termos o gatinho, podemos escrever:

```Python
print("Olá, mundo!")
```

Onde `print()` é o equivalente em Python ao `diga` em Scratch

### Loops (repetições)

No caso de loops(laços que repetem), em Scratch nós podíamos usar o bloco `sempre` ou o bloco `repita`.

Em Python, `sempre` é equivalente a
```Python
while(True):
    print("Olá, mundo!")
```
Onde `while` significa **enquanto** e `True` significa **verdadeiro**. Dessa forma, deveremos _printar_, ou seja, _imprimir_ na tela **enquanto** o que estiver dentro dos parênteses for verdadeiro. Como **verdadeiro** é sempre verdadeiro, ele vai imprimir infinitamente para sempre.

Já o segundo _loop_ é um pouco diferente. O equivalente de `repita` é:
```Python
for i in range(10):
    print("Olá, mundo!")
```
Onde `for i in range(10)` significa **para i em _intervalo_ de um a 10**, _printar_ `Olá, mundo!`. Pode parecer difícil de entender, mas isso significa que _printaremos_ 10 vezes `Olá, mundo!`.

O `for` em Python é muito poderoso e nós aprenderemos mais sobre ele no futuro.

### Variáveis

Em Scratch, nós éramos capazes de definir variáveis usando o bloco `mude [i] para [0]`. Em Python, fazemos isso apenas com:
```Python
i = 0
```

Python faz algo chamado [_inferência de tipo_](https://anotacoesdohercules.wordpress.com/2013/03/05/tipagem-fracaforte-e-inferencia-de-tipo/) que permite que o _tipo_ de dado associado à variável seja definido pela própria linguagem. Isse permite que, ao contrário de como acontece em linguagens como C ou Java, nós não temos que explicitamente dizer o que é a coisa que estamos associando a `i`. Python decide isso por nós.

Essa abordagem tem vantagens e desvantagens, mas no mundo atual onde temos computadores rápidos e grande quantidade de código compartilhado e reutilizdo, ter o tipo das variáveis inferido pela linguagem faz com que Python se destaque em simplicidade, eficiência e modularidade.

### Expressões booleanas
Em Python e Scratch, fazer uma comparação booleana é tão simples quanto:
```Python
i < 50
```

### Condicionais
Enquanto em Scratch nós usávamos condicionais usando blocos de `se - então`, em Python nós usamos:
```Python
if x < y:
    print("x é menor que y")
elif y < x:
    print("y é menor que x")
else:
    print("x é igual a y")
```
Onde `se` equivale a `if` e `senão` equivale a `else`. `elif` é uma abreviação, em Python, de `else if` que equivale a `senão se`.

### Arrays / Lists (listas)
Em Scratch nós também temos listas, que nós usamos pra guardar diversos valores dentro. Em scratch nós podemos acessa o primeiro valor de uma lista usando `item [1] de [argv]` onde nós acessamos o primeiro item de uma lista(list/array) chamado `argv`.

Em Python, fazemos isso assim:
```Python
argv[0]
```
Onde acessamos o primeiro valor (_de índice 0_) dentro da minha lista chamada `argv`.

Lembrando que o nome `argv` é um nome arbitrário. Vocês podem chamar suas variáveis e listas do que quiserem.

## Olá, mundo!
Voltando pro nosso primeiro programa,
```Python
print("Olá, mundo!")
```
Temos que entender que existe [muita coisa](http://softwareengineering.stackexchange.com/questions/313254/how-does-the-python-runtime-actually-work) acontecendo entre o que você digita na tela e o que o computador entende.

Computadores, como vimos na primeira aula, são apenas capazes de entender 0s e 1s. Como fazemos, então, para que o computador entenda o que escrevemos?

O [Interpretador](https://pt.wikipedia.org/wiki/Interpretador) de Python pega esse texto se e converte ele nisso aqui:
```
01111111 01000101 01001100 01000110 00000010 00000001 00000001 00000000
00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000
00000010 00000000 00111110 00000000 00000001 00000000 00000000 00000000
10110000 00000101 01000000 00000000 00000000 00000000 00000000 00000000
01000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000
11010000 00010011 00000000 00000000 00000000 00000000 00000000 00000000
00000000 00000000 00000000 00000000 01000000 00000000 00111000 00000000
00001001 00000000 01000000 00000000 00100100 00000000 00100001 00000000
00000110 00000000 00000000 00000000 00000101 00000000 00000000 00000000
01000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000
01000000 00000000 01000000 00000000 00000000 00000000 00000000 00000000
01000000 00000000 01000000 00000000 00000000 00000000 00000000 00000000
11111000 00000001 00000000 00000000 00000000 00000000 00000000 00000000
11111000 00000001 00000000 00000000 00000000 00000000 00000000 00000000
00001000 00000000 00000000 00000000 00000000 00000000 00000000 00000000
00000011 00000000 00000000 00000000 00000100 00000000 00000000 00000000
00111000 00000010 00000000 00000000 00000000 00000000 00000000 00000000
00111000 00000010 01000000 00000000 00000000 00000000 00000000 00000000
00111000 00000010 01000000 00000000 00000000 00000000 00000000 00000000
00011100 00000000 00000000 00000000 00000000 00000000 00000000 00000000
...
```
Agora sim o computador poderá entender o que você escreveu.

Para que ocorra essa _tradução_ entre _código de máquina_ e o código que você escreveu, muita coisa tem que acontecer. Essas coisas todas tornam a sua vida muito mais fácil, mas aumentam o tempo necessário para o processamento dos comandos. Isso faz com que Python seja uma linguagem _lenta_ em comparação com linguagens **baixo nível**.

## Cloud9
Usaremos o Cloud9 em nossa programação.

Para acessar, entre em [https://c9.io/login](https://c9.io/login) e digite o email e senha que você criou durante a aula.

No lado esquerdo da tela você encontrará escrito `Projeto ALES` e um círculo pequeno com um `+` dentro. Clique nele.

Em `Workspace name` digite o seu nome, todo em letras minúsculas seguido de um `-` e seu sobrenome, sem espaços e, novamente, seguido de um `-` escrito `sites`. No fim, deverá ser algo como `gustavo-maronato-sites`.

Depois disso, clique em `Clone workspace` e selecione `gustavomaronato/aulas-sites` e clique em `Create workspace`.

Pronto! Agora você pode acessar tudo feito em nossa aula.


## Terminal
Quando você estiver dentro do seu _workspace_ (área de trabalho, local onde vocês vão programar), você verá que na parte inferior existe um **terminal**. Nesse **terminal** você será capaz de executar comandos e, essencialmente, fazer seu código Python rodar.

Abaixo vão alguns comandos que você já deve ir se acostumando a usar:

- `ls` Comando que _**l**i**s**ta_ todos os arquivos e pastas(diretórios) que estão dentro do diretório atual do terminal.
- `mkdir <nome-do-diretório>` Comando para criar um diretório (_**m**a**k**e **dir**ectory_, em inglês) dentro do diretório atual do terminal.
- `cd <nome-do-diretório>` Comando para mudar de diretório (_**c**hange **d**irectory_, em inglês), indo para o diretório especificado.
- `rm <nome-do-arquivo>` Comando para _**r**e**m**over_, apagando, um arquivo do sistema.
- `rmdir <nome-do-diretório>` Comando para _**r**e**m**over_ um  _**dir**etório_, apagando-o, do sistema.

Lembrando, claro, do mais importante:
- `python <nome-do-arquivo>` Comando para **executar** seu código em Python.

_OBS_: Lembre-se que existem duas versões principais de Python: a **2** e a **3**. Nós utilizaremos a **3**, então, caso você queira garantir que a versão que está sendo executada é a **3**, use:
- `python3 <nome-do-arquivo>`

## Programando em Python

Comece, dentro do Cloud9, clicando em `File -> New File` para criar um arquivo novo.
Dentro dele, digite:
```Python
print("Olá, mundo!")
```

Agora clique em `File -> Save` para salvar. Ele vai pedir para que você escolha o nome do arquivo. É importante saber que para que os arquivos de Python funcionem corretamente, devemos colocar `.py` ao final do nome deles.

Vamos, então, chamar esse nosso novo arquivo de `ola.py`. Clique em salvar e pronto.

### ola.py
Nosso arquivo `ola.py` agora já pode ser executado. Pra executá-lo, basta ir até o terminal e digitar:
```
python ola.py
```
de forma que seu terminal deve estar assim, depois que você apertar enter:
```
~/workspace/ $ python ola.py
Olá, mundo!
~/workspace/ $
```

Fantástico! Nosso primeiro programa inteiramente em python funciona!

Agora vamos aprender a usar `entradas` e fornecer valores ao código.

### entrada.py
Crie um novo arquivo, seguindo as instruções acima, e nele nós teremos:
```Python
pessoa = input("Diga seu nome: ")

print("Olá, %s" % pessoa)
```
Podemos ver algumas coisas novas aqui. Em particular, vemos `pessoa = input("Diga seu nome: ")`. O que isso significa?

Como vimos em variável, se eu tiver algo do tipo `x = 5` eu estou definindo que `x` vale `5`. A mesma coisa acontece aqui, pois eu estou criando uma variável chamada `pessoa` e dizendo que ela vale `input("Diga seu nome: ")`.

Mas o que é `input("Diga seu nome: ")`? Da mesma forma que aprendemos sobre funções e aprendemos que `print( )` é uma função, podemos perceber que `input( )` também é uma função.

Pensando no termo inglês `input` que significa **entrada** no sentido de algo que você fornece ao código, podemos imaginar que `input("Diga seu nome: ")` vai pedir para que nós digitemos algo e vai **retornar** essa coisa que nós digitamos, a associando a `pessoa`.

Outra coisa nova que vemos é o `%s`. Esse símbolo de porcentagem seguido da letra `s` são especiais pois eles permitem que nós _encaixemos_ valores ao texto `"Olá, "`. Nós queremos que o nome da pessoa que escrevemos e salvamos em `pessoa` seja _encaixado_ logo após o `"Olá, "`. O `%s` irá, então, dizer pro Python que alguma variável será encaixada ali e nós dizemos pro `%s` que variável será essa logo em seguida, colocando `% pessoa` depois das àspas. Dessa forma o `%s` será substituído pelo valor de `pessoa`.

Vamos testar. Após salvar o arquivo como `entrada.py`, vamos executá-lo:
```
python entrada.py
```

Seu terminal deve estar assim:
```
~/workspace/ $ python entrada.py
Diga seu nome:
```

Digitando seu nome, nós teremos um resultado similar:
```
~/workspace/ $ python entrada.py
Diga seu nome: Maronato
Olá, Maronato
~/workspace/ $
```

Funciona! Agora você já deve ser capaz de ler entradas e processar esses dados dentro de Python usando o terminal!

### somas.py
Crie outro arquivo que nós chamaremos de `somas.py`.
Dentro dele teremos:

```Python
x = input("digite x: ")
y = input("digite y: ")

print("a soma de x com y é %s" % (x + y))
```
Salve esse código e execute.

Seu resultado pode ser, por exemplo:
```
~/workspace/ $ python somas.py
digite x: 5
digite y: 4
a soma de x com y é 54
~/workspace/ $
```
Ué? 54 não é a soma de 5 com 4. É como se nós tivéssemos _juntado_ `5` com `4` pra fazer `54`. Foi exatamente isso que aconteceu! Python simplemente juntou os dois sem _somar_ os seus valores. Isso acontece porque quando nós usamos `input( )` em Python, nós automaticamente definimos que `x` será _**texto**_. Nós não precisávamos nos preocupar com isso antes, mas agora nós temos que falar pra Python a diferença entre `5` como o _número_ `5` e `5` como o _texto_ `5`.

Para dizer pro Python que o valor que nós vamos digitar vai ser de fato um _número inteiro_, nós precisamos envolver nosso `input( )` em um `int( )`, que nada mais é que outra _função_ que **converte** um valor em um _número inteiro_. Devemos tomar cuidado, pois se não for possível escrever o valor que nós digitarmos em um _número inteiro_, nosso programa não executará. (Por exemplo, não dá pra converter a palavra `casa` em um número.).

Dessa forma, nosso código fica:

```Python
x = int(input("digite x: "))
y = int(input("digite y: "))

print("a soma de x com y é %d" % (x + y))
```
Temos uma coisa nova aqui: `%d`. Antes nós estávamos usando `%s` no `print( )` e agora estamos usando `%d`. Por quê?

Fazemos isso porque `%s` é uma referência a variáveis do tipo `string`, que nada mais são que _textos_, _cordas textuais_.

O nosso novo `%d`, (que também pode ser representado como `%i`), faz referência a variáveis do tipo `inteiro`, ou seja, _números inteiros_.

Temos outros tipos também, como os `%c` para _caracteres_, `%f` para _floats_ e etc. Veremos mais desses com o tempo.

Por agora, vamos executar novamente nosso código:

```
~/workspace/ $ python somas.py
digite x: 5
digite y: 4
a soma de x com y é 9
~/workspace/ $
```
Agora sim o valor que esperávamos!

Podemos, também, realizar outras operações como _subtração_, _multiplicação_, _divisão_ e até pegar o _resto da divisão_!

Observe os novos prints e as expressões que usamos:
```Python
x = int(input("digite x: "))
y = int(input("digite y: "))

print("a soma de x com y é %d" % (x + y))

print("a subtração de x por y é %d" % (x - y))

print("a multiplicação de x por y é %d" % (x ** y))

print("a divisão de x por y é %d" % (x / y))

print("o resto da divisão de x por y é %d" % (x % y))
```

Agora, se executarmos isso para `x = 1` e `y = 10`, temos:
```
~/workspace/ $ python somas.py
digite x: 1
digite y: 10
a soma de x com y é 11
a subtração de x por y é -9
a multiplicação de x por y é 10
a divisão de x por y é 0
o resto da divisão de x por y é 1
~/workspace/ $
```

**Mas olha só!** `a divisão de x por y é 0` não parece certo! `1` divido por `10` é `0.1`, não `0`!

Isso aconteceu pois, quando nós definimos nosso `x` e `y`, nós os definimos como _números inteiros_. Não existem números com vírgulas nos _números inteiros_, apenas nos _números racionais_. Por causa disso, a divisão de `1` por `10`, que nós **definimos** como _números inteiros_, tem que ser um _número inteiro_ também! O número inteiro mais próximo de `0.1` é `0`, logo é essa a resposta.

Mas e se eu quiser a resposta com vígula?

Pra isso nós vamos precisar definir nosso `x` e `y` como _números racionais_. Isso pode ser definido, em Python, como um [_número de ponto flutuante_](https://pt.wikipedia.org/wiki/Ponto_flutuante), ou `float`.

Nosso novo código fica:
```Python
x = float(input("digite x: "))
y = float(input("digite y: "))


print("a soma de x com y é %.0f" % (x + y))

print("a subtração de x por y é %.0f" % (x - y))

print("a multiplicação de x por y é %.0f" % (x ** y))

print("a divisão de x por y é %.2f" % (x / y))

print("o resto da divisão de x por y é %.0f" % (x % y))
```

Onde agora eu uso `%f` ao invés de `%d`. Perceba também que nós estamos usando umas coisas entre o `%` e o `f`. Como `floats` possuem vírgula, é interessante dizer pra Python quantos números depois da vígula nós queremos que apareça, caso contário vários números desnecessários aparecerão. Nós regulamos isso colocando um `.2` entre o `%` e o `f`, onde o `2` pode ser qualquer número de valores depois da vígula que queremos que apareçam.

Por exemplo, `%.0f` não mostrará **nenhum** número depois da vígula, equanto que `%.2f` mostrará **2**.

### imprecisao.py

Agora que nós já sabemos tudo sobre `floats`, vamos falar sobre a **imprecisão** deles.

Frações como `1/3` têm o resultado sendo um número que tem infinitos algarismos. No caso, `1/3 = 0,33333...`. Pra que nós salvemos esse valor no computador, teríamos que salvar **todos** os **infinitos** algarismos. Pra isso nós precisaríamos que nosso computador tivesse uma quantidade **infinita** de **memória** pra que todos esses valores fossem salvos.

Memória infinita _ainda_ não existe, então algumas pessoas inteligentes criaram uma forma de **representar** números infinitos sem salvar eles inteiros. Isso funciona até certo ponto, pois chega uma hora que essa nossa **representação** faz com que nossos números acabem sendo levemente _imprecisos_.

Vamos ver isso na prática. Crie um arquivo novo e chame-o de `imprecisao.py`, com o seguinte texto:
```Python
print(0.1 + 0.2)
```
Parece bem simples, né? `0.1 + 0.2` tem que ser `0.3`.

Porém, quando rodamos o programa, vemos:
```
~/workspace/ $ python imprecisao.py
0.30000000000000004
~/workspace/ $
```
`0.30000000000000004` definitivamente não é `0.3`, mas **_chega bem perto_**. É isso que nós chamamos de imprecisão. Não é possível escrever os valores em sua forma **absoluta**, mas nós podemos chegar bem perto.

Na prática, chegamos tão perto que essa _imprecisão_ é completamente irrelevante na vida real. Apenas em alguns casos é que nós sofremos com ela, mas sempre há como _aumentar_ essa precisão caso seja realmente necessário.

### condicionais.py
Vamos agora ir pra expressões booleanas.

Pode parecer difícil, mas é basicamente uma expressão, ou uma _pergunta_, cuja resposta pode ser apenas _verdadeiro_ ou _falso_ (`True` ou `False` em Python).

Criemos um arquivo chamado `condicionais.py` com o código:
```Python
x = int(input("Digite um número: "))

if x > 0:
   print("x é positivo")

elif x < 0:
   print("x é negativo")

elif x == 0:
    print("x é 0")
```
O que nós fazemos aqui é comparar `x` com `0` para decidir se ele é _menor que_ (`<`) `0`, _maior que_ (`>`) `0` ou _igual a_(`==`) `0`.

### logica.py
Outra coisa que podemos fazer com Python é _fazer_ algo _se outra coisa seja verdadeira ou falsa_. Em Python nós fazemos isso usando as expressões `if`, `else` e `elif`(equivalente de `else if` em Python).

Crie o arquivo `logica.py` com o código:
```Python
entrada = input("Quer mesmo fazer isso?")

if entrada == "s" or entrada == "S" or entrada == "Sim":
    print("feito")

if entrada == "n" or entrada == "N" or entrada == "Não":
    print("Não feito")
```
Nesse programa nós perguntamos ao usuário se algo deve ser feito e experamos que a resposta seja `s` **ou** `S` **ou** `Sim` para algo que **deve** ser feito e `n` **ou** `N` **ou** `Não` para algo que **não deve** ser feito.

Perceba que nós usamos um operador `or` dentro dos nossos `if`s. `or`, como deve ser experado, é a tradução de _ou_. O resultado dessa pergunta é o que parece em português:
- Se a entrada for "s" **ou** for "S" **ou** for "Sim", faça a coisa.
- Se a entrada for "n" **ou** for "N" **ou** for "Não", não faça a coisa.

Existe também o operador `and`, que é a tradução do _e_. O efeito desse operador deve vir de forma intuitiva pra você, se pensar em como o _e_ funciona no português.

### prototipo.py
Até agora nós estamos apenas usando funções que já nos foram dadas, mas e se quisermos **criar** funções?

Criando o arquivo `prototipo.py` com o código:
```Python
pessoa = input("fale seu nome: ")

def diz_ola(nome):
    print("olá, " + nome)

diz_ola(pessoa)
```
Nós podemos ver que tem algo novo aí: `def diz_ola(nome):`. Em Python, é assim que nós **def**inimos funções.

Observando o código, podemos perceber que a função tem alguns pontos-chave. Primeiro que começamos a definição com `def`. Depois disso nós falamos qual é o _nome_ da função, no caso `diz_ola`, pois é uma função que fala "Olá" para alguém dono de `nome`. Falando em `nome`, vemos que ele vem logo depois de `diz_ola` dentro de parênteses. Isso significa que `nome` é um dos *argumentos* de `diz_ola`. Ou seja, é um valor que _entra_ em `diz_ola` e que nós podemos usar.

Nós, de fato, usamos esse `nome` ao fazer `print("olá, " + nome)`.

Temos que perceber, também, que `def` e `print` não estão alinhados, ou seja, existem alguns **espaços** antes de `print`. Isso é **muito** importante, pois é a forma como definimos o [_escopo_](https://pt.wikipedia.org/wiki/Escopo_(computa%C3%A7%C3%A3o)) de nossa função, ou seja, o que _acontece_ dentro dela, efetivamente. É assim que nós definimos o que é **função** e o que não é. Nós fazíamos isso com os nossos `if`s e nossos `while` e `for` também, mas só agora é que a importância disso começa a se tornar real.

Dessa forma, quando nós, na última linha, falamos `diz_ola(pessoa)` o que está acontecendo é que estamos _chamando_ `diz_ola` e passando o _argumento_ `pessoa` que é o _nome_ de quem queremos dar olá para, que é o valor que nós pegamos com o `input`.

Fez sentido? Vamos ver em prática:
```
~/workspace/ $ python prototipo.py
fale seu nome: Maronato
olá, Maronato
~/workspace/ $
```

### quadrado.py
Nossa função em `prototipo.py` é bacana, mas é simples demais.

E se nós quiséssemos _processar_ um valor dentro dela e depois de processado, _pegar esse valor de volta_?

E se a gente precisar calcular o *quadrado* de um número (ou seja, ele vezes ele mesmo) e quisermos usar esse valor depois?

Podemos fazer isso assim, no arquivo `quadrado.py`:
```Python
x = int(input("diga um valor: "))

def quadrado(numero):
    return numero * numero

novo_numero = quadrado(x)

print("x ao quadrado é: " + str(novo_numero))
```

Aqui a gente tem uma função chamada `quadrado` que tem algo novo nela. Temos agora essa palavra nova: `return`.

Essa palavra, que traduz para _retornar_, faz justamente isso: retorna o valor definido logo depois dela para ser usado por quem **chamou** nossa função `quadrado`.

Nós podemos ver isso em `novo_numero = quadrado(x)`. Aqui a gente chama `quadrado` passando o valor `x`, que é o número que digitamos. `quadrado` processa `x` e _retorna_ o quadrado dele, cujo valor é **salvo** em `novo_numero`.

Na prática:
```
~/workspace/ $ python quadrado.py
diga um valor: 3
x ao quadrado é: 9
~/workspace/ $
```

### abstracao.py

Por último, vamos levar esses conceitos que vimos no último arquivo pro próximo nível e entender sobre **abstração**.

em um arquivo chamado `abstracao.py`, escrevemos:

```Python
x = int(input("digite um valor "))

def falar(palavra):
    print(palavra + "!!")


def tossir():
    falar("cough")

def espirrar():
    falar("atchoo")


for i in range(x):
    tossir()
    espirrar()
```

Aqui nós temos 3 funções: `falar`, que simplesmente _printa_ uma `palavra` que é passada como _parâmetro/argumento_ seguida de `!!` para dar ênfase. Temos também `tossir` que é uma função que **chama** `falar` e passa `"cough"` como argumento e `espirrar` que também **chama** `falar` e passa `"atchoo"` como argumento.

Por fim nós temos um _loop_ `for` que usa o valor de `x` que nós recebemos lá no começo do código e repete, `x` vezes, **chamando** `tossir` seguida de `espirrar`

Na prática:
```
~/workspace/ $ python abstracao.py
digite um valor 3
cough!!
atchoo!!
cough!!
atchoo!!
cough!!
atchoo!!
~/workspace/ $
```

Isso pode parecer simples, mas o que nós fazemos aqui é realmente interessante:
- Nós criamos uma função que é chamada por outra função que nós criamos e que chama outra função criada por alguém que não conhecemos: `print`

Isso mostra o real poder da programação: a capacidade de construirmos **abstrações**, ou seja códigos que englobam e usam outros códigos que fazem o mesmo com outros códigos.

Nós não precisamos saber como que `print` foi escrita. Só precisamos `chamar` ela. A mesma coisa vale pra `tossir`, que não precisa saber como que `falar` foi escrita. E `falar` não liga se foi `tossir` ou `espirrar` que chamou ela, desde que nós passemos seus _argumentos_ corretamente.

## Por fim
Aos poucos, com a abstração, nós seremos capazes de sair de coisas assim, simples como textos na tela e passaremos a ser capazes de nos conectar à internet, acessar páginas usando Python, construir páginas e até criar sites inteiros. Tudo isso, por meio de abstrações como a que fizemos agora, em escalas cada vez maiores.

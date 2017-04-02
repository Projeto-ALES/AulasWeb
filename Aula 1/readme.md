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
Onde `while` significa *enquanto* e `True` significa *verdadeiro*. Dessa forma, deveremos _printar_, ou seja, _imprimir_ na tela *enquanto* o que estiver dentro dos parênteses for verdadeiro. Como *verdadeiro* é sempre verdadeiro, ele vai imprimir infinitamente para sempre.

Já o segundo _loop_ é um pouco diferente. O equivalente de `repita` é:
```Python
for i in range(10):
    print("Olá, mundo!")
```
Onde `for i in range(10)` significa *para i em _intervalo_ de um a 10*, _printar_ `Olá, mundo!`. Pode parecer difícil de entender, mas isso significa que _printaremos_ 10 vezes `Olá, mundo!`.

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

Para que ocorra essa _tradução_ entre _código de máquina_ e o código que você escreveu, muita coisa tem que acontecer. Essas coisas todas tornam a sua vida muito mais fácil, mas aumentam o tempo necessário para o processamento dos comandos. Isso faz com que Python seja uma linguagem _lenta_ em comparação com linguagens *baixo nível*.

## Cloud9
Usaremos o Cloud9 em nossa programação.

Para acessar, entre em [https://c9.io/login](https://c9.io/login) e digite o email e senha que você criou durante a aula.

No lado esquerdo da tela você encontrará escrito `Projeto ALES` e um círculo pequeno com um `+` dentro. Clique nele.

Em `Workspace name` digite o seu nome, todo em letras minúsculas seguido de um `-` e seu sobrenome, sem espaços e, novamente, seguido de um `-` escrito `sites`. No fim, deverá ser algo como `gustavo-maronato-sites`.

Depois disso, clique em `Clone workspace` e selecione `gustavomaronato/aulas-sites` e clique em `Create workspace`.

Pronto! Agora você pode acessar tudo feito em nossa aula.

Depois de brincar com os programas, não esqueça de ir fazer as lições de casa pra aprender e treinar!

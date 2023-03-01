# Documentação Sintática da Linguagem Sue

# 1. Elementos Sintáticos.

Um programa em Sue é composto por uma ou mais funções. Uma função Sue apresenta sintaxe similar a C, conforme apresentado na seguinte regra:
``` 
funcao -> ID ID ""("" sigParams ")" "{" stms "}"
```
Onde os dois primeiros ID se refere, respectivamente, ao tipo de retorno da função e o nome da função. sigParams representa os argumentos da função. Por último temos stms que representam um ou mais comandos. Na próximo seção será apresentada os comandos da linguagem Sue.


## 1.1 Comandos da Linguagem Sue

Com relação aos comandos aceitos, Sue lida apenas com comandos de expressões, o comando de repetição while e o comando return, conforme apresentado nas seguintes regras:

```
stm → exp ";"  
      | WHILE "(" exp ")" "{" stms "}" 
      | return exp ";"

```
O comando while inicia com a palavra reservada while, seguido por uma expressão envolvida entre parênteses. Adicionalmente, ele apresenta obrigatoriamente uma sequência de comandos, envolvidos por chaves.

Quanto ao comando return ele inicia com a palavra reservada return, seguido por uma expressão. Ao seu final, é usado o delimitador ;.

## 1.2 Expressões em Sue
Sue dá suporte a expressões aritméticas de soma, multiplicação e exponenciação. Adicionalmente, também dá suporte a chamadas de função (call), atribuição de valores a variáveis (assign). Por fim, expressões também podem ser números (NUM) e variáveis (ID). A sintaxe das expressões Sue é apresentada pela seguinte regra:

```
exp → exp "+" exp | 
      exp "*" exp | 
      exp "^" exp | 
      call | 
      assign | 
      NUM | 
      ID
```

### 1.2.1 Chamadas de Função e Atribuição

Sue dá suporte a chamadas de função com e sem parâmetros. Um parâmetro de função pode ser qualquer expressão Sue. Adicionalmente, Sue permite atribuir valores a variáveis, conforme regras apresentadas a seguir:

```
call → ID "("params")" | 
       ID "(" ")"
params → exp"," params | 
         exp
assign → ID "=" exp
```


# 2. Exemplos de Código.

A seguir, alguns exemplos de código na Linguagem Sue:

```
int sumparabola(int a, int b, int c){
        return a + b + true;
    }
    int some (int a, int b){
        a = 88 + 44;
        b = 70;
        sumparabola(1, 2, 3);        
        while (true){
            c = 38;
            sumparabola(5, true, false);
            while (c){
                sumparabola(5, true, true);
            }
        }
        soma();
        sumparabolac(2);
        return true;
    }
    int sumparabolac(int a){
        return a;
    }
```

```
int some (int a, int b){ 
    a = 88 + 44; 
    b = 70; 
    sumparabola(1, 2, 3);         
    while (true){ 
        c = 38; 
        sumparabola(5, true, false); 
        while (c){ 
            sumparabola(5, true, true); 
        } 
    } 
    soma(); 
    sumparabolac(2); 
    return true; 
}
```

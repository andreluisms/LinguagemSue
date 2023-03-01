# ✨ Linguagem Sue - Elementos Léxicos

Sue é uma linguagem de programação baseada em C, usada para apresentar as diferentes etapas necessárias para o processo de compilação. A seguir, destacamos seus elementos léxicos:

#### 1. Palavras reservadas.

Sue apresenta apenas as seguintes palavras reservas: **true**, **false**, **return** e **while**. 

#### 2. Operadores

Sue apresenta os operadores aritméticos de **soma (+)**, **multiplicação**  (*) e **exponenciação (^)**. Também apresenta o **operador =** para atribuições. Sue possui a seguinte tabela de precedência, apresentada na ordem crescente de prescedência.

| Grau de Precedência | Operador | Associativade|
|:-------------------:|:--------:|:-----------:|
|          1          |     =    | Direita para Esquerda |
|          2          |     +    | Esquerda para direita |
|          3          |     *    | Esquerda para direita |
|          4          |     ^    | Direita para Esquerda |

#### 3. Delimitadores
Comandos em Sue utilizam **;** como delimitador. Parâmetros de funções utiliza **,** como delimitador. Adicionalmente, Sue utiliza os delimitadores **( )** para expressões. Por fim, também é utilizado o delimitador **{ }** para blocos de comandos. 

#### 4. Identificadores

Para identificadores, Sue apresenta regra bastante empregada em diferentes linguagens de programação. Sue aceita como identificador válido qualquer sequência de símbolos iniciada por **letras** ou **_**. Após esse simbolo inicial, o identificador pode conter **letras**, **_** e **números**. Abaixo, alguns exemplos de identifidores válidos:

```
_variavel
nome13
somar_4_vezes
```
#### 5. Números

Sue dá suporte a apenas números inteiros. Adicionalmente, Sue não faz uso de sinal positivo ou negativo. Assim, Sue só aceita números inteiros sem sinal.

#### 6. Erros
Qualquer coisa que não se enquadre em nenhum dos cinco itens apresentados, é considerado como um erro léxico. 

Adicionalmente, Sue ignora espaços em branco e tabulações. Por fim, Sue também ignora quebras de linha, mas as utiliza para informar ao léxico, em que ponto ele se encontra no processo de análise. Essa informação é recuperada através da variável **lineno**. 

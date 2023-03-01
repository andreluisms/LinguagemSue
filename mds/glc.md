# GLC da Linguagem de Programação SUE (Somente um Exemplo)
Terminais são representados pelos elementos cuja grafia está em maiúsculo, bem como 
pelos símbolos que estão entre aspas duplas (")
```
program → funcdecl | 
          funcdecl program

funcdecl → signature body

signature → ID ID ""("" sigParams ")"

sigparams → ID ID | 
            ID ID "," sigparams

body → "{" stms "}"

stms → stm  | 
       stm  stms

stm → exp ";"  | 
      WHILE "(" exp ")" body | return exp ";"

call → ID "(" params ")"

exp → exp "+" exp | 
      exp "*" exp | 
      exp "^" exp | 
      call | 
      assign | 
      NUM | 
      ID

call → ID "("params")" | 
       ID "(" ")"

params → exp"," params | 
         exp

assign → ID "=" exp
```

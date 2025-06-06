# -------------------------
# ExpressionLanguageLex.py
#----------------------
import ply.lex as lex
reservadas = {
   'while' : 'WHILE',
   'true' : 'TRUE',
   'false' : 'FALSE',
   'return' : 'RETURN'
}
tokens = ['COMMA', 'SOMA', 'ID', 'NUMBER', 'VEZES', 'POT', 'LPAREN',
          'RPAREN', 'IGUAL', 'LCHAV', 'RCHAV', 'PV', 'LESS'] + list(reservadas.values())

t_IGUAL= r'='
t_SOMA = r'\+'
t_VEZES = r'\*'
t_POT = r'\^'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COMMA = r','
t_LCHAV = r'{'
t_RCHAV = r'}'
t_LESS = r'<'
t_PV = r';'

def t_ID(t):
   r'[a-zA-Z_][a-zA-Z_0-9]*'
   t.type = reservadas.get(t.value,'ID')
   return t

def t_NUMBER(t):
   r'\d+'
   t.value = int(t.value)
   return t

def t_newline(t):
   r'\n+'
   t.lexer.lineno += len(t.value)

t_ignore = ' \t'

def t_error(t):
   print("Illegal character '%s'" % t.value[0])
   t.lexer.skip(1)


def main():
   f = open("input1.su", "r")
   lexer = lex.lex(debug=1)
   lexer.input(f.read())
   print('\n\n# lexer output:')
   for tok in lexer:
      print ('type:', tok.type, ', value:',tok.value)


if __name__ == "__main__":
   main()
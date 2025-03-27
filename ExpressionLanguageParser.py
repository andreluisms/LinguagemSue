# Rascunho da gramatica
# program → funcdecl | funcdecl program | vardecl | vardecl program
# funcdecl → signature body
# signature → id id ( sigParams)
# sigparams → ID ID | ID ID COMMA sigparams
# body → { stms }
# stms → stm  | stm  stms
# stm → exp ;  | while ( exp ) body | return exp ;
# call → id ( params )
# exp → exp + exp | exp * exp | exp ^ exp | call | assign | num | id
# call → id (params) | id ( )
# params → exp, params | exp
# assign → id = exp
import ply.yacc as yacc
from ExpressionLanguageLex import *
import SintaxeAbstrata as sa

def p_program1(p):
    '''program : funcdecl'''
    p[0] = sa.SingleFunProgram(p[1])

def p_program2(p):
    '''program : funcdecl program'''
    p[0] = sa.CompoundFunProgram(p[1], p[2])    

def p_program3(p):
    '''program : globalvardecl program'''
    p[0] = sa.CompoundVarProgram(p[1], p[2])

def p_program4(p):
    '''program : globalvardecl'''
    p[0] = sa.SingleVarProgram(p[1])

def p_program5(p):
    '''program : callglobal'''
    p[0] = sa.SingleCallProgram(p[1])
 
def p_program6(p):
    '''program : callglobal program'''
    p[0] = sa.CompoundCallProgram(p[1], p[2])

def p_vardecl(p):
    '''globalvardecl : ID IGUAL expless PV'''
    p[0] = sa.GVDConcrete(p[1], p[3])

def p_callglobal(p):
    '''callglobal : call PV'''
    p[0] = sa.CGCConcrete(sa.CallExp(p[1]))

def p_funcdecl(p):
    '''funcdecl : signature body'''
    p[0] = sa.FuncDeclConcrete(p[1], p[2])

def p_signature1(p):
    '''signature : ID ID LPAREN sigparams RPAREN'''
    p[0] = sa.SignatureConcrete(p[1], p[2], p[4])


def p_signature2(p):
    '''signature : ID ID LPAREN RPAREN'''
    p[0] = sa.SignatureConcrete(p[1], p[2], None)

def p_sigparams1(p):
    '''sigparams : ID ID'''
    p[0] = sa.SingleSigParams(p[1], p[2])

def p_sigparams2(p):
    '''sigparams :  ID ID COMMA sigparams'''
    p[0] = sa.CompoundSigParams(p[1], p[2], p[4])

def p_body1(p):
    ''' body : LCHAV stms RCHAV'''
    p[0] = sa.BodyConcrete(p[2])

def p_body2(p):
    ''' body : LCHAV RCHAV'''
    p[0] = sa.BodyConcrete(None)

def p_stms1(p):
    ''' stms : stm'''
    p[0] = sa.SingleStm(p[1])

def p_stms2(p):
    ''' stms : stm stms'''
    p[0] = sa.CompoundStm(p[1], p[2])

def p_stm1(p):
    ''' stm :  exp PV'''
    p[0] = sa.StmExp(p[1])

def p_stm2(p):
    ''' stm :  WHILE LPAREN exp RPAREN body'''
    p[0] = sa.StmWhile(p[3], p[5])

def p_stm3(p):
    ''' stm :  RETURN exp PV'''
    p[0] = sa.StmReturn(p[2])

def p_exp_assign1(p):
    ''' exp :    exp IGUAL expless'''
    p[0] = sa.AssignExp(p[1], p[3])

def p_exp_assign2(p):
    ''' exp : expless'''
    p[0] = p[1]

def p_exp_less1(p):
    '''expless : expless LESS exp1'''
    p[0] = sa.LessExp(p[1], p[3])

def p_exp_less2(p):
    '''expless : exp1'''
    p[0] = p[1]


def p_exp1_soma1(p):
    '''exp1 : exp1 SOMA exp2'''
    p[0] = sa.SomaExp(p[1], p[3])

def p_exp1_soma2(p):
    '''exp1 : exp2'''
    p[0] = p[1]

def p_exp2_vezes1(p):
   '''exp2 : exp2 VEZES exp3'''
   p[0] = sa.MulExp(p[1], p[3])

def p_exp2_vezes2(p):
   '''exp2 : exp3'''
   p[0] = p[1]

def p_exp3_pot1(p):
    '''exp3 : exp4 POT exp3'''
    p[0] = sa.PotExp(p[1], p[3])

def p_exp3_pot2(p):
    '''exp3 : exp4'''
    p[0] = p[1]

def p_exp4_call1(p):
    '''exp4 : call'''
    p[0] = sa.CallExp(p[1])

def p_exp4_call2(p):
    '''exp4 : NUMBER'''
    p[0] = sa.NumExp(p[1])

def p_exp4_call3(p):
    '''exp4 : ID'''
    p[0] = sa.IdExp(p[1])


def p_exp4_call4(p):
    '''exp4 : TRUE
            | FALSE'''
    p[0] = sa.BooleanExp(p[1])

def p_call_id_params1(p):
    '''call : ID LPAREN params RPAREN'''
    p[0] = sa.ParamsCall(p[1], p[3])


def p_call_id_params2(p):
    '''call : ID LPAREN RPAREN'''
    p[0] = sa.NoParamsCall(p[1])


def p_params_ids1(p):
    '''params : exp COMMA params '''
    p[0] = sa.CompoundParams(p[1], p[3])

def p_params_ids2(p):
    '''params : exp '''
    p[0] = sa.SingleParam(p[1])


def p_error(p):
    print("Syntax error in input!")


def main():
    f = open("input1.su", "r")
    lexer = lex.lex()
    lexer.input(f.read())
    parser = yacc.yacc()
    result = parser.parse(debug=True)


if __name__ == "__main__":
    main()
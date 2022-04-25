from AbstractVisitor import AbstractVisitor
import SymbolTable as st
from Visitor import Visitor

import SintaxeAbstrata as sa

def coercion(type1, type2):
    if (type1 in st.Number and type2 in st.Number):
        if (type1 == st.FLOAT or type2 == st.FLOAT):
            return st.FLOAT
        else:
            return st.INT
    else:
        return None

class SemanticVisitor(AbstractVisitor):

    def __init__(self):
        self.printer = Visitor()
        st.beginScope('main')

    def visitFuncDeclConcrete(self, funcDeclConcrete):
        funcDeclConcrete.signature.accept(self)
        funcDeclConcrete.body.accept(self)

    def visitSignatureConcrete(self, signatureConcrete):
        params = {}
        if (signatureConcrete.sigParams!= None):
            params = signatureConcrete.sigParams.accept(self)
            st.addFunction(signatureConcrete.id, params, signatureConcrete.type)
        else:
            st.addFunction(signatureConcrete.id, params, signatureConcrete.type)
        st.beginScope(signatureConcrete.id)
        for k in range(0, len(params), 2):
            st.addVar(params[k], params[k+1])

    def visitSingleSigParams(self, singleSigParams):
        return [singleSigParams.id, singleSigParams.type]

    def visitCompoundSigParams(self, compoundSigParams):
        return [compoundSigParams.id, compoundSigParams.type] + compoundSigParams.sigParams.accept(self)

    def visitBodyConcrete(self, bodyConcrete):
        if (bodyConcrete.stms != None):
            bodyConcrete.stms.accept(self)

    def visitSingleStm(self, singlestm):
        singlestm.stm.accept(self)

    def visitCompoundStm(self, compoundStm):
        compoundStm.stm.accept(self)
        compoundStm.stms.accept(self)

    def visitStmExp(self, stmExp):
        stmExp.exp.accept(self)

    def visitStmWhile(self, stmWhile):
        type = stmWhile.exp.accept(self)
        if (type != st.BOOL):
            stmWhile.exp.accept(self.printer)
            print ("\n\t[Erro] A expressao ", end='')
            stmWhile.exp.accept(self.printer)
            print(" eh", type, end='')
            print (". Deveria ser boolean\n")
        stmWhile.block.accept(self)

    def visitStmReturn(self, stmReturn):
        typeExp = stmReturn.exp.accept(self)
        scope = st.symbolTable[-1][st.SCOPE]
        bindable = st.getBindable(scope)
        if (typeExp != bindable[st.TYPE]):
            stmReturn.accept(self.printer)
            print('\t[Erro] O retorno da funcao', scope, 'eh do tipo', bindable[st.TYPE],end='')
            print(' no entanto, o retorno passado foi do tipo', typeExp, '\n')
        st.endScope()

    def visitAssignExp(self, assignExp):
        typeVar = assignExp.exp2.accept(self)
        if (isinstance(assignExp.exp1, sa.IdExp)):
            st.addVar(assignExp.exp1.id, typeVar)
            return typeVar
        return None

    def visitSomaExp(self, somaExp):
        tipoExp1 = somaExp.exp1.accept(self)
        tipoExp2 = somaExp.exp2.accept(self)
        c = coercion(tipoExp1, tipoExp2)
        if (c == None):
            somaExp.accept(self.printer)
            print('\n\t[Erro] Soma invalida. A expressao ', end='')
            somaExp.exp1.accept(self.printer)
            print(' eh do tipo', tipoExp1, 'enquanto a expressao ', end='')
            somaExp.exp2.accept(self.printer)
            print(' eh do tipo', tipoExp2,'\n')
        return c


    def visitMulExp(self, mulExp):
        tipoExp1 = mulExp.exp1.accept(self)
        tipoExp2 = mulExp.exp2.accept(self)
        c = coercion(tipoExp1, tipoExp2)
        if (c == None):
            mulExp.accept(self.printer)
            print('\n\t[Erro] Soma invalida. A expressao ', end='')
            mulExp.exp1.accept(self.printer)
            print(' eh do tipo', tipoExp1, 'enquanto a expressao ', end='')
            mulExp.exp2.accept(self.printer)
            print(' eh do tipo', tipoExp2,'\n')
        return c

    def visitPotExp(self, potExp):
        tipoExp1 = potExp.exp1.accept(self)
        tipoExp2 = potExp.exp2.accept(self)
        c = coercion(tipoExp1, tipoExp2)
        if (c == None):
            potExp.accept(self.printer)
            print('\n\t[Erro] Soma invalida. A expressao ', end='')
            potExp.exp1.accept(self.printer)
            print(' eh do tipo', tipoExp1, 'enquanto a expressao ', end='')
            potExp.exp2.accept(self.printer)
            print(' eh do tipo', tipoExp2,'\n')
        return c

    def visitCallExp(self, callExp):
        callExp.call.accept(self)

    def visitNumExp(self, numExp):
        if (isinstance(numExp.num, int)):
            return st.INT
        elif (isinstance(numExp.num, float)):
            return st.FLOAT

    def visitIdExp(self, idExp):
        idName = st.getBindable(idExp.id)
        if (idName != None):
            return idName[st.TYPE]
        return None

    def visitBooleanExp(self, booleanExp):
        return st.BOOL

    def visitParamsCall(self, paramsCall):
        bindable = st.getBindable(paramsCall.id)
        if (bindable != None and bindable[st.BINDABLE] == st.FUNCTION):
            typeParams = paramsCall.params.accept(self)
            if (list(bindable[st.PARAMS][1::2]) == typeParams):
                return bindable[st.TYPE]
            paramsCall.accept(self.printer)
            print("\n\t[Erro] Chamada de funcao invalida. Tipos passados na chamada sao:", typeParams)
            print('\tenquanto que os tipos definidos no metodo sao:', bindable[st.PARAMS][1::2], '\n')
        else:
            paramsCall.accept(self.printer)
            print("\n\t[Erro] Chamada de funcao invalida. O id", paramsCall.id,
                  "nao eh de uma funcao, nao foi definido ou foi definido apos esta funcao\n")
        return None

    def visitNoParamsCall(self, simpleCall):
        bindable = st.getBindable(simpleCall.id)
        if (bindable != None and bindable[st.BINDABLE] == st.FUNCTION):
            return bindable[st.TYPE]
        simpleCall.accept(self.printer)
        print("\n\t[Erro] Chamada de funcao invalida. O id", simpleCall.id, "nao eh de uma funcao, nao foi definido ou foi definido apos esta funcao\n")
        return None

    def visitCompoundParams(self, compoundParams):
        return [compoundParams.exp.accept(self)] + compoundParams.params.accept(self)

    def visitSingleParam(self, singleParam):
        return [singleParam.exp.accept(self)]

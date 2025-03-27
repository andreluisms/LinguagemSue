from abc import abstractmethod
from abc import ABCMeta

'''
Definicao de programa
Program
'''
class Program(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class CompoundFunProgram(Program):
    def __init__(self, funcDecl, program):
        self.funcDecl = funcDecl
        self.program = program
    def accept(self, visitor):
        return visitor.visitCompoundFunProgram(self)
    
class CompoundVarProgram(Program):
    def __init__(self, globalVarDecl, program):
        self.globalVarDecl = globalVarDecl
        self.program = program
    def accept(self, visitor):
        return visitor.visitCompoundVarProgram(self)
    
class CompoundCallProgram(Program):
    def __init__(self, callglobal, program):
        self.callglobal = callglobal
        self.program = program
    def accept(self, visitor):
        return visitor.visitCompoundCallProgram(self)
    
class SingleFunProgram(Program):
    def __init__(self, funcDecl):
        self.funcDecl = funcDecl
    def accept(self, visitor):
        return visitor.visitSingleFunProgram(self)

class SingleVarProgram(Program):
    def __init__(self, globalVarDecl):
        self.globalVarDecl = globalVarDecl
    def accept(self, visitor):
        return visitor.visitSingleVarProgram(self)
    
class SingleCallProgram(Program):
    def __init__(self, callglobal):
        self.callglobal = callglobal
    def accept(self, visitor):
        return visitor.visitSingleCallProgram(self)

class GlobalVarDecl(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class GVDConcrete(GlobalVarDecl):
    def __init__(self, id, exp):
        self.id = id
        self.exp = exp
    def accept(self, visitor):
        return visitor.visitGVDConcrete(self)
    
class CallGlobal(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass
    
class CGCConcrete(CallGlobal):
    def __init__(self, call):
        self.call = call
    def accept(self, visitor):
        return visitor.visitCGCConcrete(self)

'''
Declaracao de funcao
FuncDecl
'''



class FuncDecl(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class FuncDeclConcrete(FuncDecl):
    def __init__(self, signature, body):
        self.signature = signature
        self.body = body
    def accept(self, visitor):
        return visitor.visitFuncDeclConcrete(self)

'''
Assinatura de funcao
Signature
'''
class Signature(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class SignatureConcrete(Signature):
    def __init__(self, type, id, sigParams):
        self.type = type
        self.id = id
        self.sigParams = sigParams
    def accept(self, visitor):
        return visitor.visitSignatureConcrete(self)
'''
Parametros de assinatura de funcao
SigParams
'''

class SigParams(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class SingleSigParams(SigParams):
    def __init__(self, type, id):
        self.type = type
        self.id = id
    def accept(self, visitor):
        return visitor.visitSingleSigParams(self)


class CompoundSigParams(SigParams):
    def __init__(self, type, id, sigParams):
        self.type = type
        self.id = id
        self.sigParams = sigParams
    def accept(self, visitor):
        return visitor.visitCompoundSigParams(self)

'''
Corpo de uma funcao
Body
'''

class Body(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class BodyConcrete(Body):
    def __init__(self, stms):
        self.stms = stms
    def accept(self, visitor):
        return visitor.visitBodyConcrete(self)

'''
Comandos
Stms
'''

class Stms(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class SingleStm(Stms):
    def __init__(self, stm):
        self.stm = stm
    def accept(self, visitor):
        return visitor.visitSingleStm(self)

class CompoundStm(Stms):
    def __init__(self, stm, stms):
        self.stm = stm
        self.stms = stms
    def accept(self, visitor):
        return visitor.visitCompoundStm(self)

'''
Comando
Stm
'''

class Stm(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class StmExp(Stm):
    def __init__(self, exp):
        self.exp = exp
    def accept(self, visitor):
        return visitor.visitStmExp(self)

class StmWhile(Stm):
    def __init__(self, exp, block):
        self.exp = exp
        self.block = block
    def accept(self, visitor):
        return visitor.visitStmWhile(self)

class StmReturn(Stm):
    def __init__(self, exp):
        self.exp = exp
    def accept(self, visitor):
        return visitor.visitStmReturn(self)

'''
Expressoes
Exp
'''

class Exp(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class AssignExp(Exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor):
        return visitor.visitAssignExp(self)

class LessExp(Exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor):
        return visitor.visitLessExp(self)


class SomaExp(Exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor):
        return visitor.visitSomaExp(self)


class MulExp(Exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor):
        return visitor.visitMulExp(self)


class PotExp(Exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor):
        return visitor.visitPotExp(self)


class CallExp(Exp, Stm):
    def __init__(self, call):
        self.call = call

    def accept(self, visitor):
        return visitor.visitCallExp(self)

class NumExp(Exp):
    def __init__(self, num):
        self.num = num
    def accept(self, visitor):
        return visitor.visitNumExp(self)


class IdExp(Exp):
    def __init__(self, id):
        self.id = id
    def accept(self, visitor):
        return visitor.visitIdExp(self)

class BooleanExp(Exp):
    def __init__(self, boolValue):
        self.boolValue = boolValue
    def accept(self, visitor):
        return visitor.visitBooleanExp(self)

'''
Chamada de funcao
Call
'''
class Call(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class ParamsCall(Call):
    def __init__ (self, id, params):
        self.id = id
        self.params = params
    def accept(self, visitor):
        return visitor.visitParamsCall(self)

class NoParamsCall(Call):
    def __init__(self, id):
        self.id = id
    def accept(self, visitor):
        return visitor.visitNoParamsCall(self)


'''
Parametros de uma chamada de funcao
Params
'''
class Params(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class CompoundParams(Params):
    def __init__(self, exp, params):
        self.exp = exp
        self.params = params
    def accept(self, visitor):
        return visitor.visitCompoundParams(self)

class SingleParam(Params):
    def __init__(self, exp):
        self.exp = exp
    def accept(self, visitor):
        return visitor.visitSingleParam(self)



from abc import abstractmethod
from abc import ABCMeta

class AbstractVisitor(metaclass=ABCMeta):

    @abstractmethod
    def visitFuncDeclConcrete(self, funcDecl):
        pass

    @abstractmethod
    def visitSignatureConcrete(self, signature):
        pass

    @abstractmethod
    def visitSingleSigParams(self, singleSigParams):
        pass

    @abstractmethod
    def visitCompoundSigParams(self, compoundSigParams):
        pass

    @abstractmethod
    def visitBodyConcrete(self, body):
        pass

    @abstractmethod
    def visitSingleStm(self, singlestm):
        pass

    @abstractmethod
    def visitCompoundStm(self, compoundStm):
        pass

    @abstractmethod
    def visitStmExp(self, stmExp):
        pass

    @abstractmethod
    def visitStmWhile(self, stmWhile):
        pass

    @abstractmethod
    def visitStmReturn(self, stmReturn):
        pass

    @abstractmethod
    def visitAssignExp(self, assignExp):
        pass

    @abstractmethod
    def visitSomaExp(self, somaExp):
        pass

    @abstractmethod
    def visitMulExp(self, mulExp):
        pass

    @abstractmethod
    def visitPotExp(self, potExp):
        pass

    @abstractmethod
    def visitCallExp(self, callExp):
        pass

    @abstractmethod
    def visitNumExp(self, numExp):
        pass

    @abstractmethod
    def visitIdExp(self, idExp):
        pass

    @abstractmethod
    def visitBooleanExp(self, booleanExp):
        pass

    @abstractmethod
    def visitParamsCall(self, paramsCall):
        pass

    @abstractmethod
    def visitNoParamsCall(self, simpleCall):
        pass

    @abstractmethod
    def visitCompoundParams(self, compoundParams):
        pass

    @abstractmethod
    def visitSingleParam(self, singleParam):
        pass

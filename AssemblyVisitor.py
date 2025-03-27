from AbstractVisitor import AbstractVisitor
from ExpressionLanguageParser import *
import AssemblyST as st

def getAssemblyType(type = None):
    # Apenas protótipo
    # Em Sue, só é usado .word
    return ".word"

class AssemblyVisitor(AbstractVisitor):

    def __init__(self):
        st.beginScope(st.SCOPE_MAIN) #Cria escopo main
        #funcs, text e data são listas que armazenam o código assembly
        self.funcs = []  
        self.text = []  
        self.text.append(".text")
        self.text.append("    move $fp, $sp")
        self.data = set()  # Campo .data
        self.rotulos = {}  #dicionario que armazena rotulos gerados para alguns comandos e expressoes (while, exppot) 

    def novo_rotulo(self, string):
        if not string in self.rotulos:
            self.rotulos[string] = 0
        rotulo = f"{string}_{self.rotulos[string]}"
        self.rotulos[string] += 1
        return rotulo
    
    #Devolve a lista de instruções que utilizada de acordo com o escopo
    def getList(self):
        return self.text if st.getScope() == st.SCOPE_MAIN else self.funcs    
    

    def visitSingleFunProgram(self, singleFunProgram): 
        singleFunProgram.funcDecl.accept(self)

    def visitSingleVarProgram(self, singleVarProgram): 
        singleVarProgram.globalVarDecl.accept(self)

    def visitSingleCallProgram(self, singleCallProgram):
        singleCallProgram.callglobal.accept(self)

    def visitCompoundFunProgram(self, compoundFunProgram): 
        compoundFunProgram.funcDecl.accept(self)
        compoundFunProgram.program.accept(self)

    def visitCompoundVarProgram(self, compoundVarProgram): 
        compoundVarProgram.globalVarDecl.accept(self)
        compoundVarProgram.program.accept(self)

    def visitCompoundCallProgram(self, compoundCallProgram):
        compoundCallProgram.callglobal.accept(self)
        compoundCallProgram.program.accept(self)

    #Visitação de declaração de variáveis globais
    def visitGVDConcrete(self, globalVarDecl):
        name = globalVarDecl.id
        globalVarDecl.exp.accept(self)
        self.data.add((name, getAssemblyType()))
        st.addVar(name, getAssemblyType())
        self.text.append(f"    sw $v0, {name}($zero)")  # Associa valor a variável 

    #Visitação de chamada de função global
    def visitCGCConcrete(self, cgcConcrete):
        cgcConcrete.call.accept(self)

    #Visitação de chamada de função (tanto para local e global)
    def visitCallExp(self, callExp):
        code = self.getList() 
        code.append("    addi $sp, $sp, -8")  # Ajustar pilha
        st.addSP(-8)
        oldSP = st.getSP()
        code.append("    sw $ra, 0($sp)")  # Salvar endereço de retorno
        code.append("    sw $fp, 4($sp)")  # Salvar frame pointer  
        callExp.call.accept(self)
        code.append("    lw $fp, 4($sp)")  # Restaurar frame pointer
        code.append("    lw $ra, 0($sp)")  # Restaurar endereço de retorno
        code.append("    addi $sp, $sp, 8")  # Ajustar pilha de volta
        st.addSP(oldSP - st.getSP())
        st.addSP(8)    

    #Metodos de visitacao para chamada de função com parametros (os três a seguir)
    def visitParamsCall(self, paramsCall):
        code = self.getList() 
        paramsCall.params.accept(self)
        code.append(f"    jal {paramsCall.id}")  # Chamar função

    def visitSingleParam(self, singleParam):
        code = self.getList() 
        singleParam.exp.accept(self)
        st.addSP(-4)
        code.append(f"    sw $v0, {st.getSP()}($fp)")

    def visitCompoundParams(self, compoundParams):
        code = self.getList() 
        compoundParams.exp.accept(self)
        st.addSP(-4)
        code.append(f"    sw $v0, {st.getSP()}($fp)")
        compoundParams.params.accept(self)

    #Metodo de visitacao para chamada de função sem parametros
    def visitNoParamsCall(self, simpleCall):
        code = self.getList() 
        code.append(f"    jal {simpleCall.id}")  # Chamar funcao

    #Visitação de declaração de função
    def visitFuncDeclConcrete(self, funcDeclConcrete):
        funcDeclConcrete.signature.accept(self)
        funcDeclConcrete.body.accept(self)
        st.endScope()
    
    #Visitação de assinatura de função
    def visitSignatureConcrete(self, signatureConcrete):
        params = {}
        if (signatureConcrete.sigParams!= None):
            params = signatureConcrete.sigParams.accept(self)
            st.addFunction(signatureConcrete.id, params,  getAssemblyType())
        else:
            st.addFunction(signatureConcrete.id, params,  getAssemblyType())
        st.beginScope(signatureConcrete.id)
        code = self.getList()
        code.append(f"{signatureConcrete.id}:")
        code.append("    move $fp, $sp")  # Configurar o frame pointer
        if params:
            for k in range(0, len(params), 2):
                st.addVar(params[k], params[k+1])

        code.append(f"    addi $sp, $sp, {st.getSP()}")  # Ajustar pilha

    #Os dois métodos a seguir são de visitação dos parametros da assinatura de função
    def visitCompoundSigParams(self, compoundSigParams):
        code = self.getList() 
        compoundSigParams.sigParams.accept(self)
        return [compoundSigParams.id, getAssemblyType()] + compoundSigParams.sigParams.accept(self)

    def visitSingleSigParams(self, singleSigParams):
        return [singleSigParams.id,  getAssemblyType()]

    #Visitação de corpo de função
    def visitBodyConcrete(self, bodyConcrete):
        if bodyConcrete.stms:
            bodyConcrete.stms.accept(self)

    #Métodos Stm, que são utilizados para visitar cada tipo de comando
    def visitSingleStm(self, singleStm):
        singleStm.stm.accept(self)
    
    def visitCompoundStm(self, compoundStm):
        compoundStm.stm.accept(self)
        compoundStm.stms.accept(self)

    def visitStmReturn(self, stmReturn):
        stmReturn.exp.accept(self)
        self.funcs.append("    move $sp, $fp")  # Restaurar stack pointer
        self.funcs.append("    jr $ra")         # Retornar para a função chamadora
    
    def visitStmWhile(self, stmWhile):
        rotulo_inicial = self.novo_rotulo("whilestm")
        rotulo_final = self.novo_rotulo("fim_whilestm")      
        self.funcs.append(f"{rotulo_inicial}:")
        stmWhile.exp.accept(self)
        self.funcs.append(f"    beq $v0, $zero, {rotulo_final}")  # Se condição falsa, sai do loop
        stmWhile.block.accept(self)
        self.funcs.append(f"    j {rotulo_inicial}")  # Volta para o início do loop
        self.funcs.append(f"{rotulo_final}:")

    def visitStmExp(self, stmExp):
        stmExp.exp.accept(self)  

    #Visitação das expressões
    def visitAssignExp(self, assignExp):
        code = self.getList() 
        assignExp.exp2.accept(self)
        bind = st.getBindable(assignExp.exp1.id)
        if bind == None:
            st.addVar(assignExp.exp1.id, getAssemblyType())
            bind = st.getBindable(assignExp.exp1.id)
        code.append(f"    sw $v0, {bind[st.OFFSET]}($fp)")  # Atribuir variável na pilha
    
    def visitLessExp(self, lessExp):
        code = self.getList()
        # Avalia a primeira expressão e armazena na pilha
        lessExp.exp1.accept(self)
        code.append("    addi $sp, $sp, -4")
        st.addSP(-4)
        code.append("    sw $v0, 0($sp)")
        # Avalia a segunda expressão
        lessExp.exp2.accept(self)
        # Recupera o primeiro operando
        code.append("    lw $t0, 0($sp)")
        code.append("    add $sp, $sp, 4")  # Libera espaço na pilha
        st.addSP(4)
        # Comparação: se $t0 < $v0, então $v0 = 1, senão $v0 = 0
        code.append("    slt $v0, $t0, $v0")


    def visitSomaExp(self, somaExp):
        code = self.getList()
        somaExp.exp1.accept(self)  # Avalia a primeira expressão
        code.append("    addi $sp, $sp, -4")  # Aloca espaço na pilha
        st.addSP(-4)
        code.append("    sw $v0, 0($sp)")  # Empilha o resultado
        somaExp.exp2.accept(self)  # Avalia a segunda expressão
        code.append("    lw $t0, 0($sp)")  # Recupera o valor salvo
        code.append("    add $sp, $sp, 4")  # Libera espaço da pilha
        st.addSP(4)
        code.append("    add $v0, $t0, $v0")  # Soma os valores

    def visitMulExp(self, mulExp):
        code = self.getList()        
        mulExp.exp1.accept(self)  # Avalia a primeira expressão
        code.append("    addi $sp, $sp, -4")
        st.addSP(-4)
        code.append("    sw $v0, 0($sp)")
        mulExp.exp2.accept(self)  # Avalia a segunda expressão
        code.append("    lw $t0, 0($sp)")
        code.append("    add $sp, $sp, 4")
        st.addSP(4)   
        code.append("    mul $v0, $t0, $v0")  # Multiplica os valores

    def visitPotExp(self, potExp):
        code = self.getList()

        # Avalia a base e salva na pilha
        potExp.exp1.accept(self)
        code.append("    addi $sp, $sp, -4")
        st.addSP(-4)
        code.append("    sw $v0, 0($sp)")

        # Avalia o expoente
        potExp.exp2.accept(self)
        code.append("    lw $t0, 0($sp)")  # Recupera a base
        code.append("    add $sp, $sp, 4")  # Libera espaço na pilha
        st.addSP(4) 
        code.append("    move $t1, $v0")  # $t1 = expoente

        # Inicializa o resultado
        code.append("    li $v0, 1")  

        # Criando rótulos para o loop de exponenciação
        rotulo_laco = self.novo_rotulo("potexp")
        rotulo_final = self.novo_rotulo("fim_potexp")

        # Loop de exponenciação
        code.append(f"{rotulo_laco}:")
        code.append(f"    beq $t1, $zero, {rotulo_final}")  # Se expoente == 0, sai
        code.append("    mul $v0, $v0, $t0")  # Multiplica resultado pela base
        code.append("    sub $t1, $t1, 1")  # Decrementa expoente
        code.append(f"    j {rotulo_laco}")  # Volta para o início do loop
        code.append(f"{rotulo_final}:")  # Fim da exponenciação
        
    def visitNumExp(self, numExp):
        code = self.getList() 
        code.append(f"    li $v0, {numExp.num}")
    
    def visitIdExp(self, idExp):
        code = self.getList() 
        idName = st.getBindable(idExp.id)
        if (idName != None):
            if (st.getScope(idExp.id) == st.SCOPE_MAIN):
                code.append(f"    lw $v0, {idExp.id}($zero)")
            else:
                code.append(f"    lw $v0, {idName[st.OFFSET]}($fp)")
    
    def visitBooleanExp(self, booleanExp):
        code = self.getList() 
        value = 1 if booleanExp.boolValue == "true" else 0
        code.append(f"    li $v0, {value}")

    #gera código assembly
    def get_code(self):
        finalcode = []
        if self.data:
            for globalVar in self.data:
                finalcode.insert(0, f"    {globalVar[0]}: {globalVar[1]} 0")
            finalcode.insert(0,".data")
        finalcode = finalcode + self.text
        finalcode.append("    j end")
        finalcode = finalcode + self.funcs
        finalcode.append("\nend:\n    li $v0, 10\n    syscall")
        return "\n".join(finalcode)

def main():
    f = open("input3.su", "r")
    lexer = lex.lex()
    lexer.input(f.read())
    parser = yacc.yacc()
    result = parser.parse(debug=False)
    print("#Gera Assembly")
    assemblyvisitor = AssemblyVisitor()
    result.accept(assemblyvisitor)
    print(assemblyvisitor.get_code())

if __name__ == "__main__":
    main()
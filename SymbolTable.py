#Dicionario que representa a tabela de simbolos.
symbolTable = []
INT = 'int'
FLOAT = 'float'
BOOL = 'boolean'
TYPE = 'type'
PARAMS = 'params'
BINDABLE = 'bindable'
FUNCTION = 'fun'
VARIABLE = 'var'
SCOPE = 'scope'
# Se DEBUG = -1, imprime conteudo da tabela de símbolos após cada mudança
DEBUG = 0
Number = [INT, FLOAT]

def printTable():
    global DEBUG
    if DEBUG == -1:
        print('Tabela:', symbolTable)

def beginScope(nameScope):
    global symbolTable
    symbolTable.append({})
    symbolTable[-1][SCOPE] = nameScope
    printTable()

def endScope():
    global symbolTable
    symbolTable = symbolTable[0:-1]
    printTable()

def addVar(name, type):
    global symbolTable
    symbolTable[-1][name] = {BINDABLE: VARIABLE, TYPE : type}
    printTable()

def addFunction(name, params, returnType):
    global symbolTable
    symbolTable[-1][name] = {BINDABLE: FUNCTION, PARAMS: params, TYPE : returnType}
    printTable()

def getBindable(bindableName):
    global symbolTable
    for i in reversed(range(len(symbolTable))):
        if (bindableName in symbolTable[i].keys()):
            return symbolTable[i][bindableName]
    return None

def main():
    global DEBUG
    DEBUG = -1
    print('\n# Criando escopo main')
    beginScope('main')
    print ('\n# Adicionando Vinculavel funcao some')
    addFunction('some', ['a', INT, 'b', INT], INT)
    print('\n# Criando escopo some')
    beginScope('some')
    print('\n# Adicionando var a do tipo int')
    addVar('a', INT)
    print('\n# Adicionando var b do tipo int')
    addVar('b', INT)
    print('\n# Consultando bindable')
    print(str(getBindable('sumparabola')))
    print('\n# Consultando bindable')
    print(str(getBindable('some')))
    print('\n# Removendo escopo some')
    endScope()

if __name__ == "__main__":
    main()
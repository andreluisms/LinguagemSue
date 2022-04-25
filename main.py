from ExpressionLanguageLex import *
from ExpressionLanguageParser import *

lexer = lex.lex()
#
# # Test it out
data = '''
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
 '''
data2 = '''
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
'''
lexer.input(data2)
parser = yacc.yacc()
result = parser.parse(debug=False)
print ("#realiza a analise semantica")
visitor = sv.SemanticVisitor()

print("#imprime o programa que foi passado como entrada")
visitor = vis.Visitor()
for r in result:
  r.accept(visitor)
from Componentes import Componentes
from Analizador import AnalizadorLexico
from Reportes import Reportes

cadena = open('entrada.form').read()

lexico = AnalizadorLexico()
lexico.analizar(cadena)
lexico.imprimirTokens()
tokens = lexico.listaTokens
errores = lexico.listaErrores
Reportes().repTokens(tokens)
Reportes().repErrores(errores)
cmp = Componentes()
componentes = cmp.getComponentes(tokens)
print(componentes)
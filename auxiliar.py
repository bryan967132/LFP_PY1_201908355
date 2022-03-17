from Componentes import Componentes
from Analizador import AnalizadorLexico
from Reportes import Reportes
from Formulario import Formulario

cadena = open('formulario3.form').read()

lexico = AnalizadorLexico()
lexico.analizar(cadena)
lexico.imprimirTokens()
lexico.imprimirErrores()
tokens = lexico.listaTokens
errores = lexico.listaErrores
#Reportes().repTokens(tokens)
#Reportes().repErrores(errores)
cmp = Componentes()
componentes = cmp.getComponentes(tokens)
Formulario().generar(componentes,cadena)
print(componentes)
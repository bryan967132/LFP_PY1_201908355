from Analizador import AnalizadorLexico

cadena = open('entrada.form').read()

lexico = AnalizadorLexico()
lexico.analizar(cadena)
lexico.imprimirTokens()
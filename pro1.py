from Analizador import AnalizadorLexico

cadena = open('entrada.form').read()

lexico = AnalizadorLexico()
lexico.analizar(cadena)
lexico.imprimirTokens()
tokens = lexico.listaTokens
componentes = []
for i in range(len(tokens)):
    componente = {}
    if tokens[i].tipo == 'reservada_tipo' and tokens[i + 3].lexema == 'etiqueta':
        componente[tokens[i].lexema] = tokens[i + 3].lexema
        componente[tokens[i + 6].lexema] = tokens[i + 9].lexema
        componentes.append(componente)
    if tokens[i].tipo == 'reservada_tipo' and tokens[i + 3].lexema == 'texto':
        componente[tokens[i].lexema] = tokens[i + 3].lexema
        componente[tokens[i + 6].lexema] = tokens[i + 9].lexema
        componente[tokens[i + 12].lexema] = tokens[i + 15].lexema
        componentes.append(componente)
    if tokens[i].tipo == 'reservada_tipo' and tokens[i + 3].lexema == 'grupo-radio':
        componente[tokens[i].lexema] = tokens[i + 3].lexema
        componente[tokens[i + 6].lexema] = tokens[i + 9].lexema
        gruporadio = []
        for x in range(i + 16,len(tokens)):
            if tokens[x].lexema == ']':
                break
            if tokens[x].tipo == 'valor':
                gruporadio.append(tokens[x].lexema)
        componente[tokens[i + 12].lexema] = gruporadio
        componentes.append(componente)
    if tokens[i].tipo == 'reservada_tipo' and tokens[i + 3].lexema == 'grupo-option':
        componente[tokens[i].lexema] = tokens[i + 3].lexema
        componente[tokens[i + 6].lexema] = tokens[i + 9].lexema
        gruporadio = []
        for x in range(i + 16,len(tokens)):
            if tokens[x].lexema == ']':
                break
            if tokens[x].tipo == 'valor':
                gruporadio.append(tokens[x].lexema)
        componente[tokens[i + 12].lexema] = gruporadio
        componentes.append(componente)
    if tokens[i].tipo == 'reservada_tipo' and tokens[i + 3].lexema == 'boton':
        componente[tokens[i].lexema] = tokens[i + 3].lexema
        componente[tokens[i + 6].lexema] = tokens[i + 9].lexema
        componente[tokens[i + 12].lexema] = tokens[i + 15].lexema
        componentes.append(componente)

print(componentes)
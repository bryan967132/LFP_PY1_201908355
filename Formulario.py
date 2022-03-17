import webbrowser
class Formulario:
    def __init__(self):
        self.text = 0
        self.radio = 0
        self.select = 0
        self.iframe = """
					<div id="iframeEvento"></div>"""
        self.getelementsbyidtext = ''
        self.getqueryselectorradio = ''
        self.getelementsbyidselect = ''

    def generar(self,componentes,contenido):
        html = self.getInicioHTML()

        for componente in componentes:
            if componente['tipo'] == 'etiqueta':
                html += self.getLabel(componente)
            elif componente['tipo'] == 'texto':
                html += self.getInputText(componente)
            elif componente['tipo'] == 'grupo-radio':
                html += self.getRadio(componente)
            elif componente['tipo'] == 'grupo-option':
                html += self.getSelect(componente)
            elif componente['tipo'] == 'boton':
                html += self.getButton(componente)
        
        html += self.iframe
        html += self.getScript()
        html += self.getFinHTML()
        open('Formulario.html','w').write(html)
        self.writeEntrada(contenido)
        webbrowser.open('Formulario.html')
    
    def getScript(self):
        self.condicion = ''
        if self.select > 0:
            self.condicion += """
								if("""
            for i in range(1,self.select + 1):
                self.condicion += 'options' + str(i) + ' != "Elija una opcion"'
                if i >= 1 and i < self.select:
                    self.condicion += ' && '

            self.accion = """
									info = ''"""
            for i in range(1,self.text + 1):
                self.accion += """
									info += text""" + str(i) + " + '<br>'"
            for i in range(1,self.radio + 1):
                self.accion += """
									info += radios""" + str(i) + " + '<br>'"
            for i in range(1,self.select + 1):
                self.accion += """
									info += options""" + str(i) + " + '<br>'"
            self.accion += """
                                    localStorage.setItem('eslainfo',info)
									document.getElementById('iframeEvento').innerHTML = '<iframe src="Formulario/iframeInfo.html" width="100%" height="300"></iframe>'"""
            self.condicion += ') {'
            self.condicion += self.accion + """
								}"""
        else:
            self.condicion += """
								info = ''"""
            for i in range(1,self.text + 1):
                self.condicion += """
								info += text""" + str(i) + " + '<br>'"
            for i in range(1,self.radio + 1):
                self.condicion += """
								info += radios""" + str(i) + " + '<br>'"
            self.condicion += """
                                localStorage.setItem('eslainfo',info)
								document.getElementById('iframeEvento').innerHTML = '<iframe src="Formulario/iframeInfo.html" width="100%" height="300"></iframe>'"""
        javascript = """
					<script>
                        function eventoInfo() {
                            try {""" + self.getelementsbyidtext + self.getqueryselectorradio + self.getelementsbyidselect + self.condicion + """ 
                            }catch (error) {}
                        }
                        function eventoEntrada() {
    						document.getElementById('iframeEvento').innerHTML = '<iframe src="Formulario/iframeEntrada.html" width="100%" height="300"></iframe>'
						}
					</script>"""
        return javascript
    
    def getButton(self,diccionario):
        html = """
                    <div class="container-login100-form-btn m-b-20">
						<div class="wrap-login100-form-btn">
							<div class="login100-form-bgbtn"></div>
							<button type="button" class="login100-form-btn" onclick=\"""" + self.getEvento(diccionario) + """\">
								""" + self.getValue(diccionario) + """
							</button>
						</div>
					</div>"""
        return html
    
    def getEvento(self,diccionario):
        for key in diccionario:
            if key == 'evento':
                if diccionario['evento'] == 'entrada':
                    return 'eventoEntrada()'
                elif diccionario['evento'] == 'info':
                    return 'eventoInfo()'
        return ''
    
    def getSelect(self,diccionario):
        self.select += 1
        html = """
                    <div class="wrap-select100 m-b-10">
						<label class="label-input100">""" + self.getValue(diccionario) + """</label>
						<select id=\"opciones""" + str(self.select) + """\" class="select100">
							<option disabled selected>Elija una opcion</option>""" + self.getOptions(diccionario['valores']) + """
						</select>
					</div>"""
        self.getelementsbyidselect += """
                                options""" + str(self.select) + """ = document.getElementById('opciones""" + str(self.select) + """').options[document.getElementById('opciones""" + str(self.select) + """').selectedIndex].value"""
        return html

    def getOptions(self,lista):
        html = ''
        for option in lista:
            html += """
                            <option>""" + option + """</option>"""
        return html

    def getRadio(self,diccionario):
        self.radio += 1
        html = """
                    <div class="m-b-10">
						<label class="label-input100">""" + self.getValue(diccionario) + """</label>
						<div class="radio100">""" + self.getGroupRadio(diccionario['valores']) + """
						</div>
					</div>"""
        self.getqueryselectorradio += """
								radios""" + str(self.radio) + """ = document.querySelector('input[name = \"radios""" + str(self.radio) + """\"]:checked').value"""
        return html
    
    def getGroupRadio(self,lista):
        html = ''
        for radio in lista:
            html += """
                            <div>
								<input id=\"radio""" + radio + """\" name=\"radios""" + str(self.radio) + """\" type="radio" value=\"""" + radio + """\">
								<label class="label-input100" for="radioMasculino">""" + radio + """</label>
							</div>"""
        return html
    
    def getInputText(self,diccionario):
        self.text += 1
        html = """
                    <div class="wrap-input100 m-b-20">
						<input id=\"text""" + str(self.text) + """\" class="input100" type="text" placeholder=\"""" + self.getPlaceHolder(diccionario) + """\" value=\"""" + self.getValue(diccionario) + """\">
						<span class="focus-input100" data-symbol="&#9998;"></span>
					</div>"""
        self.getelementsbyidtext += """
								text""" + str(self.text) + """ = document.getElementById('text""" + str(self.text) + """').value"""
        return html
    
    def getValue(self,diccionario):
        for key in diccionario:
            if key == 'valor':
                return diccionario['valor']
        return ''
    
    def getPlaceHolder(self,diccionario):
        for key in diccionario:
            if key == 'fondo':
                return diccionario['fondo']
        return ''

    def getLabel(self,diccionario):
        html = """
                    <div class="m-b-10">
						<label class="label-input100">""" + self.getValue(diccionario) + """</label>
					</div>"""
        return html
    
    def getInicioHTML(self):
        html = """<!DOCTYPE html>
<html lang="en">
<head>
	<title>Formulario</title>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<link rel="icon" type="image/png" href="Formulario/images/logousac.png"/>
	<link rel="stylesheet" type="text/css" href="Formulario/css/util.css">
	<link rel="stylesheet" type="text/css" href="Formulario/css/main.css">
</head>
<body>
	
	<div class="limiter">
		<div class="container-login100" style="background-image: url('Formulario/images/bg-01.jpg');">
			<div class="wrap-login100 p-l-55 p-r-55 p-t-65 p-b-54">
				<form class="login100-form validate-form">"""
        return html
    
    def getFinHTML(self):
        html = """
                </form>
			</div>
		</div>
	</div>
</body>
</html>"""
        return html

    def writeEntrada(self,contenido):
        html = """<!DOCTYPE html>
<html lang="en">
<head>
	<title>Formulario</title>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<link rel="icon" type="image/png" href="images/logousac.png"/>
	<link rel="stylesheet" type="text/css" href="css/util.css">
	<link rel="stylesheet" type="text/css" href="css/main.css">
</head>
<body>
	
	<div class="limiter">
		<div class="container-login100" style="background-image: url('images/bg-01.jpg');">
			<div class="wrap-login100 p-l-55 p-r-55 p-t-65 p-b-54">
				<form class="login100-form validate-form">
					<div class="m-b-10">
						<label id="archivo_entrada_contenido" style="font-size: 10px" class="label-input100"></label>
					</div>
				</form>
			</div>
		</div>
	</div>
	<script>
		entrada_ordenada = ''
		entrada = `""" + contenido + """`
		for(var i = 0; i < entrada.length; i++) {
			entrada_ordenada += entrada[i]
			if(entrada[i] == ' ') {
				entrada_ordenada += '&nbsp;'
			}
			if(entrada[i] == '\\n') {
				entrada_ordenada += '<br>'
			}
		}
		document.getElementById('archivo_entrada_contenido').innerHTML = entrada_ordenada
	</script>
</body>
</html>"""
        open('Formulario/iframeEntrada.html','w').write(html)
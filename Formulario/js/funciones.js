function evento(theevento) {
    if(theevento == 'info') {
        document.getElementById('iframeEvento').innerHTML = '<iframe src="Formulario/iframeInfo.html" width="100%" height="300"></iframe>'
    }else if(theevento == 'entrada'){
        document.getElementById('iframeEvento').innerHTML = '<iframe src="Formulario/iframeEntrada.html" width="100%" height="300"></iframe>'
    }
}
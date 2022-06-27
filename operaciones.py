inputText1 = Element("inputText1")
inputText2 = Element("inputText2")

salidasuma = Element("salidasuma")
salidaresta = Element("salidaresta")
salidamultiplicacion = Element("salidamultiplicacion")
salidadivision = Element("salidadivision")

def clear(*args, **kwargs):
    inputText1.clear()
    inputText2.clear()
    salidasuma.clear()
    salidaresta.clear()
    salidamultiplicacion.clear()
    salidadivision.clear()

def calcular(*args, **kwargs):
    totalsuma = int(inputText1.value) + int(inputText2.value)
    salidasuma.write(totalsuma)
    totalresta = int(inputText1.value) - int(inputText2.value)
    salidaresta.write(totalresta)
    totalmultiplicacion = int(inputText1.value) * int(inputText2.value)
    salidamultiplicacion.write(totalmultiplicacion)    
    totaldivision = int(inputText1.value) / int(inputText2.value)
    salidadivision.write(totaldivision)
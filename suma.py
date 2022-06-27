inputText1 = Element("inputText1")
inputText2 = Element("inputText2")

output = Element("output")

def clear(*args, **kwargs):
    inputText1.clear()
    inputText2.clear()
    output.clear()

def suma(*args, **kwargs):
    totalsuma = int(inputText1.value) + int(inputText2.value)
    output.write(totalsuma)
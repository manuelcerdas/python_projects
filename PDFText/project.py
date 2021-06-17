import PyPDF2
import re
import json

keys = ["Articulo","Cantidad","Precio Unitario"]

pdfFileObj =  open("data/data.pdf","rb")
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
pageObj = pdfReader.getPage(0)
data = pageObj.extractText()
data = data.replace(chr(10),"")
data = data.replace(": ",":")
data = data.replace(" :",":")
data = data.replace(", ",",")
z = re.findall(":[A-Z 0-9 a-z]+:",data)
for elem in z:
    newelem = elem
    for llave in keys:
        newelem = newelem.replace (llave,chr(10)+llave)
    data = data.replace (elem,newelem)

data = data.split(chr(10))
arrayData = []
jsonData = {}
jsonLine = {}
for line in data:
    jsonLine = {}
    tuples = line.split(",")
    for elem in tuples:
        tuple = elem.split(":")
        jsonLine[tuple[0].strip()] = tuple[1].strip()
    arrayData.append(jsonLine)

jsonData["entries"] = arrayData

out_file = open("data/result.json", "w") 
    
json.dump(jsonData, out_file, indent = 6) 
    
out_file.close() 



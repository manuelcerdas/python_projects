

with open("templates/one_column.html") as f:
    lines = f.read()

tokens=[]    
processingToken = False
token = ""
prevChar=""
      
for char in lines:
    if char=="{":
        if prevChar == "{":
            processingToken = True
            prevChar = ""
        else: 
            prevChar = "{"
    elif char=="}":
        prevChar = ""
        if processingToken:
            processingToken = False
            tokens.append(token)
            token = ""
    else:
        prevChar = ""            
        if processingToken:
            token = token + char

print (tokens)
                

    

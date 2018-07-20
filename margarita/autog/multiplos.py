multiplo= []
multiplo1= []
numeros = 1
contador = 1    
while contador < 1000:
    if numeros % 3 == 0:
        multiplo.append(numeros)   
    elif numeros % 5 == 0:
        multiplo1.append(numeros)
    numeros= numeros + 1
    contador= contador + 1
suma= 0
suma2=0
for i in multiplo:
    suma= suma + i
for e in multiplo1:
    suma2= suma2 + e
total= suma+suma2
print(total)

    
    

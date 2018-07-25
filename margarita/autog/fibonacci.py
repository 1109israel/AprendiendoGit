a0=0
a1=1
a3=0
contador=1
numeros=[]
while a3 <= 4000000:
    a3=a0+a1
    a0=a1
    a1=a3
    if a3 <= 4000000:
        if a3 % 2 == 0:
            numeros.append(a3)
    contador=contador+1
suma=0
for i in numeros:
    suma= suma + i
print(suma)
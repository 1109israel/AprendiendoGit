numeros= input()
a= numeros.replace(',',' ')
n= a.split()
contador=0
lista= []
for y in range(len(n)):
    multi= n[contador]
    b= int(multi)
    lista.append(b)
    contador= contador + 1

x= sorted(lista)

if lista == x:
    print(True)
else:
    print(False)
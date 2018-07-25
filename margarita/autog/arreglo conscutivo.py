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

max= max(lista)  
min= min(lista)
z= max + 1
nvlista= list(range(min,z))

m= len(lista)
w= len(nvlista)
print(w-m)

    




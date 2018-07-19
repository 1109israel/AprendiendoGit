x=input()
a= x.replace(',', ' ')
y=a.split('  ')
lista=[]
for a in y:
    lista.append(int(a))#aqui solo agrego mi numero convirtiendolo en entero
#print(lista)
jeje=len(lista)-1#aqui le resto 1 a una posicion
lis=[]
o=0
for i in range(lista[0], lista[jeje]-jeje):#aqui solo le resto los numeros que ya estoy utilizando, en este caso son 2 y a esa posisicon se le resta,si es 10 entomces seria 8
    lis.append("ok")
    o+=1
#print(lis)
print(len(lis))

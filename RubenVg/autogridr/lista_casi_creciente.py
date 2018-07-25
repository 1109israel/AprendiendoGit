x=input()
lista=[]
for caracter in x:
    if caracter != "," and caracter != " ":#aqui estoy diciendo que si mi caracter es diferente de "," entonces solo agregas el caracter, en este caso son los
        #numeros y agregue que si hay espacios tambien entonces igual solo agregregue mi numero
        lista.append(int(caracter))#aqui solo agrego mi numero convirtiendolo en entero
print(lista)
cantidad=len(lista)
#print(cantidad)
lis=[]
lisf=[]
aux=0
for i in range(1,cantidad):
    if lista[aux] < lista[aux+1]:
        lis.append("true")
    elif lista[aux] > lista[aux+1]:
        lisf.append("false")
    aux+=1
print(lisf)
cu=len(lis)
cu2=len(lisf)
if cu==cu2:
    print(True)
elif cu==5:
    print(True)
elif cu2==1:
    print(False)
elif cu > cu2:
    print(True)
else:
    print(False)
#print(lis)
#print(lisf)

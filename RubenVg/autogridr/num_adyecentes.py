lista=[3, 12, 5, 1, -12, 9, 8]
aux=0
for i in range(0,6):
    #agrego un rango para que acepte todos los valores
    x=lista[aux]*lista[aux+1]#aqui le digo que el contador aux se va agregando cada vez que se repita el ciclo
    lista.append(x)#aqui solo agrego los numeros a la lista
    aux+=1
maximo=max(lista)#y aqui solo agarro el maximo
print(maximo)
    #x=lista[aux]*lista[aux+1]
#print(x)
numeros= input()
if numeros == '':
    print()
else:
    a= numeros.replace(',',' ')
    n= a.split()
    contador=0
    lista= []
    for y in range(len(n)):
        multi= n[contador]
        b= int(multi)
        lista.append(b)
        contador= contador + 1

    lista2= set(lista)
    print(list(lista2))

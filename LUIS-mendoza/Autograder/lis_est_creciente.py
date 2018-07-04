def numeros():
    '''Haz un programa que determine si una lista es estrictamente
    creciente, esto significa que todos sus elementos van en orden
    consecutivo, sin que ninguno se repita.:'''
    linea = input()
    lista = []
    lista_nueva = []
    creciente = True
    for c in linea:
        if c != "," and c != " ":
            lista.append(int(c))
    for numero in lista:
        if numero not in lista_nueva:
            lista_nueva.append(numero)
    for i in range(0,len(lista)):
        for j in range(i+1,len(lista)):
            if lista[j] < lista[i]:
                creciente = False
    print(creciente)
               
numeros()
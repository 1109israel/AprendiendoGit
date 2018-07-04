def numeros():
    '''Escribe un programa que transforme una cadena de elementos
    separados por comas, en una lista sin elementos repetidos:'''
    linea = input()
    lista = []
    lista_nueva = []
    for c in linea:
        if c != "," and c != " ":
            lista.append(int(c))
    for numero in lista:
        if numero not in lista_nueva:
            lista_nueva.append(numero)
    if len(lista_nueva)>0:
        print(lista_nueva)
               
numeros()
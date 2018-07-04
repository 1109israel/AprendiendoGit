def numeros():
    '''Escribe un programa que transforme una cadena de elementos
    separados por comas, en una lista:'''
    linea = input()
    lista = []
    lista_nueva = []
    for c in linea:
        if c != "," and c != " ":
            lista.append(int(c))
    print(lista)
numeros()
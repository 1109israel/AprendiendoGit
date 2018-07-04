def numeros():
    '''si tenemos una lista de elementos, si podemos quitarle uno y
    solo uno de los elementos y la lista que resulta es creciente,
    entonces es una lista casi creciente.'''
    linea = input()
    lista = []
    for i in linea:
        if i != "," and i != " ":
            lista.append(i)
    pos1 = 2
    pos2 = 1
    v = 0
    f = 0
    if len(lista)<=3:
        if lista[1]>lista[0] and lista[2]>lista[0]:
            print("True")
        else:
            print("False")
    else:
        while pos1 <= len(lista)-1:
            if lista[pos1]>lista[pos2]:
                v += 1
                pos1 += 1
                pos2 += 1
            else:
                f += 1
                pos1 += 1
                pos2 += 1
        if v>f:
            print("True")
        else:
            print("False")
        
numeros()
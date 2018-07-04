def arreglo_consecutivo():
    '''Calcular el número mínimo de estatuas adicionales necesarias:'''
    linea = input()
    lista = []
    cont = 0
    for c in linea:
        if c != "," and c != " ":
            lista.append(int(c))
    lista.sort()
    min = lista[0]
    max = lista[len(lista)-1]
    for i in range(min,max):
        if i not in lista:
            cont += 1
    print(cont)        
    
    
arreglo_consecutivo()
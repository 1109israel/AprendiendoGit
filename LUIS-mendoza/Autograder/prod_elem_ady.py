def adyacentes():
    '''Dado una lista de enteros, encuentra el número más grande que
    resulte del producto de números adyacentes.'''
    lista = [3, 12, 5, 1, -12, 9, 8]
    mayor=0
    for i in range(len(lista)-1):
        n = lista [i] * lista [i+1]
        if n>mayor:
            mayor=n
    print(n)
    
adyacentes()
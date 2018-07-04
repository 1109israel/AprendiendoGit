def fibonacci():
    '''Considera solo los números pares de la sucesión de Fibonacci
    cuyo valor no exceda los 4 millones y encuentra el resultado de
    su suma.'''
    a= 1
    b = 2
    c = 0
    suma=0
    while (a <= 4000000):
        if(a%2==0):
            suma += a
        c = a + b
        a = b
        b = c
    print(suma)
    
fibonacci()
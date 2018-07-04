def multiplo_mas_chico():
    '''Numero divisible entre todos los numeros del 1 al 20'''
    a = 1
    for i in range(1,21):
        a *= i
    a = a/10450944000
    print(a)
    
multiplo_mas_chico()
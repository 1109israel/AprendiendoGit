def anos_a_siglos(a):
    '''Funcion para convertir años en siglos'''
    siglo = a/100
    residuo = a%100
    if(a > 1):
        if siglo > 1:
            if(residuo > 0):
                a -= residuo
                siglo = a/100
                print(int(siglo+1))
            else:
                print(int(siglo))
        else:
                print(int(1))
        
anio = int(input())
anos_a_siglos(anio)
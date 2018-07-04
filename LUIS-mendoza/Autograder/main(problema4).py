def divisores(numero):
    ''' Hallar los divisores del numero.'''
    
    divisores = []
    for i in range (numero):
        if numero % (i+1) == 0:
            divisores.append(i+1)
    print(divisores)
    
num = int(input())
divisores(num)

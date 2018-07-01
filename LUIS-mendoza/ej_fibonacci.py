ar = open("fibonacci.txt","a")
def fibonacci_or(lim):
    a= 0
    b = 1
    c = 0
    cont = 2
    print(a,b,end = ' ')
    ar.write('%s'%a+"\t")
    ar.write('%s'%b+"\t")
    
    while cont < lim:
        c = a + b
        a = b
        b = c
        print(c, end = ' ')
        cont += 1
        ar.write('%s'%c+"\t")
    ar.write("\n")
def fibonacci(a,b):
    lim = int(input("\nIngresa el limite para la serie: "))
    c = 0
    cont = 2
    print(a,b,end = ' ')
    ar.write('%s'%a+"\t")
    ar.write('%s'%b+"\t")
    while (cont < lim):
        c = a + b
        a = b
        b = c
        print(c, end = ' ')
        cont += 1
        ar.write('%s'%c+"\t")
    ar.write("\n")
'''Ejercicios fibonacci.'''
opc = 1
while opc != 0:
    opc = input("[1]\n[2]\n[0] Salir\n\nOprime la opcion que quieres: ")
    if opc == '1':
        l = int(input("\nIngresa el limite para la serie: "))
        fibonacci_or(l)
        print("\n")
        
    elif opc == '2':
        fn = int(input("\nIngresa el primer numero para la serie: "))
        sn = int(input("\nIngresa el segundo numero para la serie: "))
        fibonacci(fn,sn)
        print("\n")
    elif opc == '0':
        break
    else:
        print("\nIngresa una opcion valida")
ar.close()
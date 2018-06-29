var = open("Serie_fibonacci.txt","a")
def fibonacci_uno(limite):
    a= 0
    b = 1
    c = 0
    contador = 2
    print(a,b,end = ' ')
    var.write('%s'%a+"\t")
    var.write('%s'%b+"\t")
    
    while contador < limite:
        c = a + b
        a = b
        b = c
        print(c, end = ' ')
        contador += 1
        var.write('%s'%c+"\t")
    var.write("\n")
def fibonacci(a,b):
    limite = int(input("Ingresa el limite para la serie: "))
    c = 0
    contador = 2
    print(a,b,end = ' ')
    var.write('%s'%a+"\t")
    var.write('%s'%b+"\t")
    while (contador < limite):
        c = a + b
        a = b
        b = c
        print(c, end = ' ')
        contador += 1
        var.write('%s'%c+"\t")
    var.write("\n")

opcion = 1
while opcion != 0:
    print('1. Serie fibonnacci')
    print('2. Serie fibonnacci con numero de tu eleccion')
    print('0. Salir')
    opcion = input("opcion deseada: ")
    if opcion == '1':
        limite = int(input("Ingresa el limite deseado para la serie: "))
        fibonacci_uno(limite)
        print("\n")
        
    elif opcion == '2':
        primer_numero = int(input("Ingresa el primer numero para la serie: "))
        segundo_numero = int(input("Ingresa el segundo numero para la serie: "))
        fibonacci(primer_numero,segundo_numero)
        print("\n")
    elif opcion == '0':
        exit()
    else:
        print("\nIngresa una opcion valida")
var.close()
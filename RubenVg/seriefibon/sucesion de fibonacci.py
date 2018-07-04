print("************ BIENVENIDO ************")
print("1. sucesion de fibonacci original")
print("2. sucesion de fibonacci con numeros elegidos")
print("teclea otro numero si quieres salir")
opc=int(input("Elige una opcion: "))
if opc==1:
    cont=0
    numero=1
    penultimo=0
    ultimo=0
    while cont <= 10:
        penultimo=ultimo
        ultimo=numero
        numero=penultimo+ultimo
        print(numero)
        cont+=1
elif opc==2:
    cont=0
    numero=int(input("elige un numero: "))
    penultimo=int(input("elige el otro numero: "))
    ultimo=0
    while cont <= 10:
        penultimo=ultimo
        ultimo=numero
        numero=penultimo+ultimo
        print(numero)
        cont+=1
else:
    exit()
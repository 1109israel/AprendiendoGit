
numero=1
penultimo=0
ultimo=0
suma=0
while numero < 4000000:
    penultimo=ultimo
    ultimo=numero
    numero=penultimo+ultimo
    print(numero)
    if numero%2==0:
        suma+=numero
        #4613732
print(suma)
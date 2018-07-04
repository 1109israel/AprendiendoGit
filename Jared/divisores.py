numero = int(input(''))
lista = []
divisor = 0
for i in range(1, numero):
    divisor += 1
    if numero % divisor == 0:
        agregar = lista.append(divisor)
agregarN = lista.append(numero)
print(lista)
             
             
             
divisores= []
numero= int(input())
contador= 1
for n in range(numero):
    if numero % contador == 0:
        divisores.append(contador)
    contador += 1
print(divisores)    
 
    
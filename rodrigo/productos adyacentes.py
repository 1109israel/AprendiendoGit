lista = [3, 12, 5, 1, -12, 9, 8]
x = 0
y = 1
z = 2
z1 = lista[0] * lista[1]
z2 = lista[6] * lista[5]
lista2 = [z1, z2]
while y < 5:
    x1 = lista[x] * lista[y]
    x2 = lista[y] * lista[z]
    x += 1
    y += 1
    z += 1
print (max(lista2))
numo = input('')
num = numo.replace(',',' ')
lista = num.split()
lis = []
for nume in lista:
    int(nume)
    x = int(nume)
    lis.append(x)
y = min(lis)
z = max(lis)
z1 = z + 1
lis1 = list(range(y,z1))
print(len(lis1) - len(lis))
numo = input('')
num = numo.replace(',',' ')
lista = num.split()
lis = []
for nume in lista:
    int(nume)
    x = int(nume)
    lis.append(x)
print(lis)
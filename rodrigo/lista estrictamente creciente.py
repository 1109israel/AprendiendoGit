numo = input('')
num = numo.replace(',',' ')
lista = num.split()
lis = []
con = 1
c = 0
y = 0
z = 1
for nume in lista:
    int(nume)
    x = nume
    lis.append(x)
while con <= len(lis) and z <= (len(lis)-1):
    if (lis[y]) <= (lis[z]):
        con += 1
        y += 1
        z += 1
        c += 1
##    if (lis[y]) > (lis[z]):
    else:
        con += 1
        y += 1
        z += 1
        c -= 1
if c == (len(lis)-1):
    print(True)
else:
    print(False)
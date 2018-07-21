numo = input('')
num = numo.replace(',',' ')
lista = num.split()
lis = []
lis1 = []
lis2 = []
for nume in lista:
    int(nume)
    x = nume
    lis2.append(x)
    if x  not in lis:
        lis.append(x)
    else:
        lis1.append(x)
##        if x in lis1:
##            lis1.append(x)
if len(lis1) > 0:
    print(False)
else:
    print(True)
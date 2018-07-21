numo = input('')
num = numo.replace(',',' ')
lista = num.split()
lis = []
for nume in lista:
    x = int(nume)
    if x not in lis:
        lis.append(x)
con = False
while len(lis) > 0 and con == False:
        print(lis)
        con = True

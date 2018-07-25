numero = int(input(''))

lis = []
divisor = 1
while divisor <= numero:
    if numero % divisor == 0:
        lis.append(divisor)
        divisor += 1
    else:
        divisor += 1
print(lis)
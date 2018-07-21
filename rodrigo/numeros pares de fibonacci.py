num1 = 1
num2 = 2
num4 = 0
contador = 0
while contador < 4000000:
    num3 = num2 + num1
    num1 = num2
    num2 = num3
    contador = num3
    if num3 % 2 == 0:
        num5 = num3 + num4
        num4 = num5
num6 = num5 + 2
print (num6)
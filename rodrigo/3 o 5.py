num = 1
num4 = 0

num1 = 3
num2 = 5

num3 = 0
while num < 1000:
    if num % num1 == 0 or num % num2 == 0:
        num3 = num + num4
        num4 = num3
        num += 1
    else:
        num += 1
print (num3)
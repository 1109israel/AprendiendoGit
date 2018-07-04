numeros = 1
contadorn = 1    
while contadorn <= 100:
    if numeros % 15 == 0:
        print("FizzBuzz")
    elif numeros % 3 == 0:
        print("Fizz")
    elif numeros % 5 == 0:
        print("Buzz")
    else:
        print(numeros)
    numeros= numeros + 1
    contadorn= contadorn + 1
    
    
    

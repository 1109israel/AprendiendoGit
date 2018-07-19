for num in range(1,101):#aqui hacemos que haga un rango donde recorra del numero 1 al 102
    if num %15 == 0:
        print("FizzBuzz")
    elif num %3 == 0:
        print("Fizz")
    elif num %5 == 0:
        print("Buzz")
    else:
        print(num)#aqui ponemos que imprima los numeros de ese ciclo que n o tengan nada qe ver con las condiciones del if
     

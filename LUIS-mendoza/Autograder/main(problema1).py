def multiplos_de_3_y_5():
    '''Aqui sabemos si el numero es multiplo de 3 o de 5 o de ambos'''
    for i in range(1,101):
        if (i%3==0) and (i%5==0):
            print("FizzBuzz")
            i += 1
        elif (i%3==0):
            print("Fizz")
            i += 1
        elif (i%5==0):
            print("Buzz")
            i += 1
        else:
            print(i)
            
multiplos_de_3_y_5()
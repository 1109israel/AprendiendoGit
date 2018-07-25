#Dado un año,
#imprime el siglo en el que se encuentra. El primer siglo va desde el año 1 hasta el año 100,
#el segundo desde el año 101 hacia arriba e inclusive el año 200, etc.
an=int(input(""))
multi=an*0.01
a=int(multi)
g=an
if g <= 100: #ponemos esto al principio para que primero verifique si al año que pusimos sea del siglo 1,si no que ejecute otra de las dos funciones
    print("1")
elif a%multi == 0:#aqui la traduccion seria,si "a" o sea un entero(el siglo),por ejemplo 17 cabe entre en año 1700 y el residuo es 0 entonces solo imprime el entero
    print(a)
else:
    print(a+1)#y aqui seria que si el residuo no es 0,entonces solo se le aumentara un uno

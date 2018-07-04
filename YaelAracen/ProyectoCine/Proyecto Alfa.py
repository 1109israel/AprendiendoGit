with open("usuarios.txt") as usuarios:
    usuario = usuarios.readlines()

usuario1= usuario[0]
usuario2= usuario[1]
usuario3= usuario[2]
    
u1 = usuario1.split("|")
user1 = u1[0].strip()
password1 = u1[1].strip()

u2 = usuario2.split("|")
user2 = u2[0].strip()
password2 = u2[1].strip()

u3 = usuario3.split("|")
user3 = u3[0].strip()
password3 = u3[1].strip()

print("************************************")
print("*          INICIAR SESION          *")
print("************************************")
print("\n")
print("[Intento 1 de 3]")
nombre = input("Usuario: ")
contraseña = input("Contraseña: ")
    

if user1 == nombre and password1 == contraseña:
    print("Bienvenido", user1)
elif user2 == nombre and password2 == contraseña:
    print("Bienvenido", user2)
elif user3 == nombre and password3 == contraseña:
    print("Bienvenida", user3)
    
else:
    print("\n")
    print("[Intento 2 de 3]")
    nombre = input("Usuario: ")
    contraseña = input("Contraseña: ")
    if user1 == nombre and password1 == contraseña:
        print("Bienvenido", user1)
    elif user2 == nombre and password2 == contraseña:
        print("Bienvenido", user2)
    elif user3 == nombre and password3 == contraseña:
        print("Bienvenida", user3)
    else:
        print("\n")
        print("[Intento 3 de 3]")
        nombre = input("Usuario: ")
        contraseña = input("Contraseña: ")
        if user1 == nombre and password1 == contraseña:
            print("Bienvenido", user1)
        elif user2 == nombre and password2 == contraseña:
            print("Bienvenido", user2)
        elif user3 == nombre and password3 == contraseña:
            print("Bienvenida", user3)
        else:
            exit()
print("\n")        
print("************************************")
print("*             CineOax              *")
print("************************************")
print("\n")

input("Presione enter para continuar")
print("\n")

with open("peliculas.txt") as peliculas:
    pelicula = peliculas.readlines()
    
    
diccionario ={}
contador = 1
respuesta = 1
while respuesta != 0:
    print("******************** CARTELERA ********************")
    for pelis in pelicula:
         diccionario[contador] = pelis.split("|")[0]
         print(contador,".",pelis.split("|")[0].strip())
         contador += 1
    print("\n")
    print("Seleccione la opcion deseada (0 para salir)")
    respuesta = int(input("Pelicula:" ))
    print(">PELICULA: ",diccionario[respuesta])
    if respuesta == 1 or respuesta == 2 or respuesta == 3:
        boletos = int(input("¿Cuántos boletos quiere? "))
        contador = 1
        total = 0
        for i in range(boletos):
            print("Edad de la persona",contador,":")
            edades = int(input("")) 
            contador += 1
            if edades > 18:
                total += 100
            else:
                total += 50
    print("PELICULA: ",diccionario[respuesta].strip())            
    print("TOTAL: ",total)
    print("\n")
    print("Disfrute la funcion")
    contador = 1

    



    


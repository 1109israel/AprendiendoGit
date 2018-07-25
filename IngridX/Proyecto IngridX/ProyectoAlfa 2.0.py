opcion=0
while opcion != 3:
#Menú principal
    print("**********************************************")
    print("***MENÚ***")
    print("1. Inciar Sesión")
    print("2. Ver la cartelera")
    print("3. Salir")
    opcion= int(input("Seleccione la opción deseada: "))
#Lista de Contactos
    
#Si desea agregar un nuevo número
    if opcion==1:
        print("***********************************")
        print("*         Inicio de sesión        *")
        print("***********************************")
        with open("usuarios.txt") as archivo1:
            usuarios=archivo1.readlines()

        diccionarioUsuarios={}
        diccionarioContraseñas={}
        contador=0

        for nombre in usuarios:
            diccionarioUsuarios[contador]=nombre.split("|")[0]
            diccionarioContraseñas[contador]=nombre.split("|")[1]
            contador+=1
            
        for nombres in diccionarioContraseñas:
            diccionarioContraseñas[nombres]=diccionarioContraseñas[nombres].strip()
            
        precio=0    
        precioTotal=0    
        intentos=1
        while intentos<=3:
            print("Intento", intentos, "de 3: ")
            nombreDeUsuario=input("Usuario: ")
            contraseñaDeUsuario=input("Contraseña: ")
            intentos+=1
            for w in diccionarioUsuarios:
                if intentos>=4:
                    print("Tus intentos se han agotado. Inténtalo de nuevo más tarde.")
                    exit()
                elif nombreDeUsuario==diccionarioUsuarios[w] and contraseñaDeUsuario==diccionarioContraseñas[w]:
                    intentos=4
                    print("***********************************")
                    print("*            Cartelera            *")
                    print("***********************************")
                    
                    with open("peliculas.txt") as archivo2:
                        peliculas=archivo2.readlines()
                        
                    diccionarioPeliculas={}
                    contadores = 1
                    for pelicula in peliculas:
                        diccionarioPeliculas[contadores]= pelicula.strip()
                        print(contadores, ".-", pelicula.strip())
                        contadores+=1
                      
                    numeroDePelicula=int(input("Seleccione el número de película que quiera ver (Presione 0 para salir): "))
                    
                    if numeroDePelicula >=1:
                        nombreDePelicula=diccionarioPeliculas[numeroDePelicula]
                        print("Ustede eligió ver", nombreDePelicula)
                        personas=int(input("Introduzca el número de boletos que desea comprar: "))
                        aux=1
                    elif numeroDePelicula == 0:
                        exit()
                        
                    cantidadDePersonas=personas
                    personas=1
                    while cantidadDePersonas>=1:
                        print("Dime la edad de la persona", personas, ":")
                        edades=int(input(" "))
                        cantidadDePersonas-=1
                        personas+=1
                        if edades<12:
                            precio=50
                            print("Esta persona tiene el 50% de descuento.")
                        elif edades>12:
                            precio=100
                            print("Esta persona paga completo.")
                        precioTotal=precioTotal+precio
        print("El total a pagar es", precioTotal, "y disfrute de", nombreDePelicula)
#Si desea ver la lista de contactos
    elif opcion==2:
        print("***********************************")
        print("*            Cartelera            *")
        print("***********************************")
                    
        with open("peliculas.txt") as archivo2:
            peliculas=archivo2.readlines()
                        
        diccionarioPeliculas={}
        contadores = 1
        for pelicula in peliculas:
            diccionarioPeliculas[contadores]= pelicula.strip()
            print(contadores, ".-", pelicula.strip())
            contadores+=1        
#Si desea salir del programa
    else:
        print("!Adiós!")
        exit()
                    
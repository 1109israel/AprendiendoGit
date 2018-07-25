
# INICIA PROGRAMA
lista=[]
opción=0
while opción!=2:
    print("*********MENÚ*********")
    print("1.- Iniciar sesión")
    print("2.- Salir")
    print("\n")

    opción=int(input("Número de la opción deseada: "))
    
    if opción==1:
        with open("usuarios.txt") as archivo:
            usuarios=archivo.readlines()
    
        diccionario={}
        diccionario2={}
        contador=0
        for usuario in usuarios:
            diccionario[contador]=usuario.split("|")[0]
            diccionario2[contador]=usuario.split("|")[1]
    
            contador+=1

        for usuario2 in diccionario2:
            diccionario2[usuario2]=diccionario2[usuario2].strip()


#Inicio de sesión
        print("******************************")
        print("*       INICIAR SESIÓN       *")
        print("******************************\n")


        precio=0
        precioTotal=0
        intentos=1
        while intentos<=3:
            print("[Intento",intentos,"de 3]")
            usuario=input("Usuario: ")
            contraseña=input("Contraseña: ")
            intentos+=1
            for q in diccionario:
                if usuario==diccionario[q] and contraseña==diccionario2[q]:
                    intentos=4
                    print("\n")
                    print("******************************")
                    print("*         CARTELERA          *")
                    print("******************************\n")
                        
                    with open("peliculas.txt") as archivo:
                        peliculas=archivo.readlines()
                
            
                    lista={}
                    contador=1
                    for pelicula in peliculas:
                        lista[contador]=pelicula.strip()
                        print(contador,". ",pelicula.strip().upper())
                        contador+=1
               
                    print("\n")
                    opción=int(input("Número de la película que desea ver (0 para salir): "))
                    nombrePelícula=lista[opción].upper()

                    if opción>=1:
                        boletos=int(input("¿Cuántos boletos desea comprar?: "))
                    elif opción==0:
                        exit()

                    contador=1
                    while boletos>0:
                        print("Edad de la persona ",contador,":")
                        edades=int(input(""))
                        contador+=1
                        boletos-=1
                    
                    
                        if edades<12:
                            print("El cliente tiene el 50% de descuento")
                            precio=50
                        elif edades>12:
                            print("El cliente paga boleto completo")
                            precio=100
                        
                        precioTotal=precioTotal+precio

                elif intentos>4:
                    print("Agotaste tus intentos. ¡Bye!")
                    exit()
                    
        print("\n")
        print("La película que verá es",nombrePelícula, "y el total a pagar es",precioTotal,)
        print("\n")
    
    if opción==2:
        print("Adiós")
with open('Usuarios.txt') as usuarios:
    usuario=usuarios.readlines()
    dicc={}
    dicc2={}
    contfor=1
    for contra in usuario:#este es un ciclo for,y sirve para guardar los datos que tenemos en el archivo y en este caso separar lados
        dicc2[contfor]= contra.split('|')[0]
        dicc[contfor]= contra.strip().split('|')[1]
        contfor +=1
    print(dicc)
    print(dicc2)
with open('Cartelera.txt') as cartelera:
    carteleras=cartelera.readlines()
    diccpelis={}
    contfor2=1
    for contrapeli in carteleras:#igual aqui en este for sirve para separarlos
        diccpelis[contfor2]=contrapeli.split(',')[0]
        contfor2 +=1
    print(diccpelis)
        
contadorwhile=3
while contadorwhile >=1:
    usua=input("escribe tu usuario: ")
    contrain=input("escribe tu contra: ")
    for jeje in dicc:
        if usua==dicc2[jeje] and contrain==dicc[jeje]:
            print("******** BIENVENIDO********")
            print("Elige una opcion (teclea 0 para salir)")
            
            for opc in diccpelis:#este for sirve para que muestre todas las peliculas, en una lista
                print(opc,".",diccpelis[opc])#Existen diversas formas de recorrer un diccionario. Es posible recorrer sus claves y usar esas claves para acceder a los valores.
            
            res=int(input("¿que pelicula quieres ver?: "))
            
            if res==1 or res==2 or res==3 or res==4 or res==5:
                print("tu pelicula es ",diccpelis[res])
                boletos=int(input("¿cuantos boletos desea comprar? "))
                contawhileuno=1
                vaso=0#esto se puede usar,aqui se inicializa una variable en cero,como un contador,y entonces cada vez que se repita el ciclo va agregar la cantidad depende de como
                #se cumplan las condiciiones de if, anotalo cabron 
                while contawhileuno<=boletos:
                    edad=int(input("cuantos años tienes? "))
                    if edad<12:
                        vaso+=50#este
                    else:
                        vaso+=100# y este
                    contawhileuno+=1
                print("el total a pagar es ",vaso,"y la pelicula es:",diccpelis[res])
            else:
                print("adios bb")
                exit()
        else:
            print("intentalo otra vez")
    
    contadorwhile -=1

    print("te quedan", contadorwhile ,"intentos de 3")
print("usted no deberia estar aqui")


import os
with open("usuarios.txt") as users:
    usuarios=users.readlines()

with open("peliculas.txt") as pelis:
    peliculas=pelis.readlines()

diccionario={}
diccionario1={}
contador=0
for i in usuarios:
    diccionario[contador]=i.split('|')[0]
    diccionario1[contador]=i.split('|')[1]
    contador+=1
    
for j in diccionario1:
    diccionario1[j]=diccionario1[j].strip()
    

#CABEZERA
print("**********************************")
print("*     BIENVENIDOS A CINEOAX      *")
print("*  INICIA SESION PARA CONTINUAR  *")
print("**********************************")

#LOGIN
acceso=False
pos=0
intentos=3
clave=1
while acceso==False and intentos>0:
    print("| Tienes ",intentos,"intentos |")
    user=input("INGRESA EL USUARIO: ")
    for usuario in diccionario:
        if user==diccionario[usuario]:
            pos=usuario
    pasword=input("INGRESA LA CONTRASEÑA: ")
    for contraseña in diccionario1:
        if pasword==diccionario1[contraseña]:
            clave=contraseña
    if pos==clave:
        acceso=True
    else:
        intentos-=1
        
os.system("cls")    
#DENTRO DEL SISTEMA
opcion=1
personas=0
edad=0
total=0
edadDescuento=12
costoBoleto=100
contador=1
diccionariop={}
contador=1

for i in peliculas:
    diccionariop[contador]=i.strip()
    contador+=1


while acceso==True and opcion != 0:
    print("******PELICULAS EN CARTELERA******")
    for x in diccionariop:
        print(x,". ",diccionariop[x])
    opcion= int(input("INGRESA EL NUMERO DE LA PELICULA QUE DESEA VER (0 PARA SALIR): "))
    if opcion==1:
        peli=diccionariop[opcion]
        peli=peli.upper()
        print("SELLECIONASTE VER",peli)
        personas= int(input("INGRESA EL NUMERO DE PERSONAS: "))
        total=personas*100
        for i in range (personas):
            print("INGRESA LA EDAD DE LA PERSONA ",i+1,": ",end='')
            edad = int(input())
            if edad < edadDescuento:
                total-=50
        print("TOTAL A PAGAR: ",total)
        print("DISFRUTA TU PELICULA")

            
    elif opcion == 2:
        peli=diccionariop[opcion]
        peli=peli.upper()
        print("SELLECIONASTE VER",peli)
        personas= int(input("INGRESA EL NUMERO DE PERSONAS: "))
        total=personas*100
        for i in range (personas):
            print("INGRESA LA EDAD DE LA PERSONA ",i+1,": ",end='')
            edad = int(input())
            if edad < edadDescuento:
                total-=50
        print("TOTAL A PAGAR: ",total)
        print("DISFRUTA TU PELICULA")
            
    elif opcion==3:
        peli=diccionariop[opcion]
        peli=peli.upper()
        print("SELLECIONASTE VER ",peli)
        personas= int(input("INGRESA EL NUMERO DE PERSONAS: "))
        total=personas*100
        for i in range (personas):
            print("INGRESA LA EDAD DE LA PERSONA ",i+1,": ",end='')
            edad = int(input())
            if edad <= edadDescuento:
                total-=50
        print("TOTAL A PAGAR: ",total)
        print("DISFRUTA TU PELICULA")
         
    elif opcion==0:
        exit()
    else:
        print("LA OPCION INGRESADA NO ES VALIDA")
    input("PULSA ENTER PARA CONTINUAR...")
    os.system("cls")
        
if acceso==True:
    print("VUELVE A USAR EL PROGRAMA PARA INGRESAR...")
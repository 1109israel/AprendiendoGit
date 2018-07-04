with open('usuarios.txt') as archivo:
    usuarios= archivo.readlines()
with open('peliculas.txt') as peli:
    pelicula= peli.readlines()
    
##variables para usuarios: 
diccionario={}
contador=1
##variables para pelicula:
car=0
car2=1
menu=0
cartel={}
contadorp=1
contadori=1
##variables para boleto
boleto= 100
contadorc= 1
c=0
n=0
m=0
for peliculas in pelicula:
    peli= pelicula[car]
    cartel[car2]= peli.strip('\n')
    car= car + 1
    car2= car2 + 1

for usuario in usuarios:
    usu= usuario.split('|')[0]
    clave= usuario.split('|')[1]
    diccionario[usu]= clave.strip('\n')


while contador<=3:
    print('[Intento', contador, 'de 3]')
    usuario= input('Usuario: ')
    contra= input('Contraseña: ')
    for key in diccionario:
        if key==usuario and diccionario[key]==contra:
            print('\t''--------------------------')
            print('\t''+  Bienvenido a CineOax  +')
            print('\t''--------------------------')
            print('\n''>Usuario: ', usuario)
            while menu != 10:
                print('\t''---------------')
                print('\t''+  Cartelera  +')
                print('\t''---------------''\n')
                for key in cartel:
                    print(contadorp,'.',cartel[key])
                    contadorp= contadorp+1
                opcion= int(input('\n''Seleccione una pelicula (0 para salir): '))
                contadorp=1
                for key in cartel:
                    if opcion == key:
                        eleccion= cartel[key]
                        print('\n''> Película:', eleccion)
                        cantadori= contadori + 1
                        clientes=[]
                        p= int(input('\n''Cantidad de boletos: '))
                        for pp in range(p):
                            persona= int(input(f'Edad persona {contadorc}:' ))
                            contadorc= contadorc + 1
                            clientes.append(persona)
                        contadorc= 1
                        for cliente in clientes:
                            if clientes[c] <= 12:
                                n= n+1
                                c= c+1
                            else:
                                m= m+1
                                c= c+1
                        pago= boleto * m
                        pago1= (boleto*0.5) * n
                        total= pago + pago1
                        print('\n''\n''Su película es: ', eleccion)
                        print('Su total a pagar es: ', total)
                        print('¡Gracias!')
                        c=0
                        n=0
                        m=0
                if opcion == 0:
                    exit()
    if  key!=usuario and diccionario[key]!=contra:
        contador= contador+1
    

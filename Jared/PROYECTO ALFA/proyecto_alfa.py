
print('**************************************')

print('*   Bienvenido a la app de CIENOAX   *')

print('**************************************')

with open('usuarios.txt') as archivo:
    usuarios = archivo.readlines()
    base_usuarios = {}
    base_contraseñas = {}
    contador=1

    for pos in usuarios:
        base_usuarios[contador] = pos.split('|')[0].strip()
        base_contraseñas[contador] = pos.split('|')[1].strip()
        contador+=1
intentos =1
while intentos <= 3:

    print('intento',intentos,'de 3')
    pedir_usuario = input('Usuario: ')
    pedir_contraseña = input('Contreseña: ')
    intentos+=1

    if intentos == 4:
        exit()
   
    else:   
        for control in base_contraseñas:
            if pedir_usuario == base_usuarios[control] and pedir_contraseña == base_contraseñas[control]:
                intentos =4
                repetir=0
                while repetir ==0:
                    with open('peliculas.txt') as archivos:
                        estrenos = archivos.readlines()
                        estrenosPelis = []
                        contadorPeliculas = 1
                        print('-----Cartelera-----')
                        for cartelera in estrenos:
                            estrenos= cartelera.split()
                            estrenos= cartelera.strip()
                            print(contadorPeliculas,'.',estrenos)
                            contadorPeliculas +=1
                        print('si deseas salir (presiona 0)')    
                        pelicula_deseada= int(input('cual es el numero de la pelicula que deseas ver : '))
                        
                        if pelicula_deseada >=1:
                            personas = int(input('cuantas personas que veran la funcion: '))
                            conatdorpers = 1
                            costo = 0
                            while conatdorpers <= personas:
                                edades = int(input('edad de la(s) persona(s): '))
                                if edades<=12:
                                    costo+=50
                                elif edades>12:
                                    costo+=100
                                conatdorpers+=1
                            print('   ')
                            print('Su total es de:', costo, 'pesos')
                            print('   ')
                            print('DISTRUTEN LA FUNCION')
                        elif pelicula_deseada ==0:
                            exit()
                        
                                
                    

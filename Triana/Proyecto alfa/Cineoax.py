#Primero abrí y lei todos mis archivos
with open ('cuentas.txt') as cuentas:
    nombres = cuentas.readlines()
with open ('movies.txt') as cartelera:
    peliculas = cartelera.readlines()
#Aquí declaré todas las variables y diccionarios que utilizaré a lo largo del código
dicc_usuarios = {}
movies = {}
p=1
intentos=1
cuenta=0
contraseña=0
acc=False
num_bol=1
total=0
precio=0
respuesta=1
#Como dejé los diccionarios vacíos aquí con los ciclos for llené los diccionarios según los archivos que leí
for  cuenta in nombres:
    usuarios=cuenta.split('|')[0]
    password=cuenta.split('|')[1]
    dicc_usuarios[usuarios]=password.strip('\n')
#Usé el .strip() para quitarle el salto de linea
#Empieza el programa para el usuario
print('*****Bienvenido a la app de Cineoax*****\n')
print('*****Ingresa tu cuenta*****\n')
print('************************************************************')
#Mientras que los intentos sean menores a 3 y el acceso sea falso se seguirá repitiendo el ciclo
while intentos<=3 and acc==False:
        print('intento', intentos, 'de 3 \n')
        cuenta=input('Escribe tu nombre de usuario: ')
        contraseña=input('Introduce tu contraseña: ')
        intentos +=1
#El usuario dio sus datos el ciclo for de abajo junto a su bloque van a recorrer mi diccionario y van a decir qué string es correcto
        for llave in dicc_usuarios:
#Si la cuenta es igual a alguna de las llaves y la contraseña es la dependencia de esa llave entonces el acceso se volverá verdadero y hará que el ciclo while se termine
            if (cuenta==llave and contraseña==dicc_usuarios[llave]):
                acc=True           
print('************************************************************* \n')
print('Bienvenido,', cuenta,'\n')
#Ya que se sabe que la cuenta y la contraseña están bien el acceso se vuelve verdadero, entonces el ciclo while como el acceso ya no es falso se va a acabar y pasará al if de abajo donde al ser verdadero seguirá con la siguiente parte del programa, la cartelera if acc==True:
while acc==True:
    print('********Cartelera******** \n')
    for pelicula in peliculas:
        movies[p] = pelicula.strip('\n')
        print(p,'.-', pelicula.strip('\n'))
        p +=1
    respuesta=int(input('Elige el número de película que deseas ver o elige 0 para salir: '))
    if respuesta==0:
        exit()
    print('Excelente, elegiste:', movies[respuesta])
    boletos=int(input('¿Cuántos boletos quieres?'))
    while num_bol<=boletos:
        edadPersona=int(input('Edad de la persona: '))
        num_bol +=1
        if edadPersona>=12:
            precio = precio + 100
        else:
            precio = precio + 50
        total=precio    
    print('El total a pagar es', total, '\n')
    print('Difrute la función')
    input('pulse cualquier letra para continuar')
exit()


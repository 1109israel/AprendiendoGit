with open ('usuarios.txt') as cuentas:
    nombres = cuentas.readlines()
with open ('peliculas.txt') as cartelera:
    peliculas = cartelera.readlines()
dicc_usuarios = {}
usuarios=[]
movies = {}
p=1
intentos=1
cuenta=0
contraseña=0
for  cuenta in nombres:
    dicc_usuarios[cuenta.split('|')[0]] =cuenta.split('|')[1]
for pelicula in peliculas:
    movies[p] = pelicula
    p +=1
print('*****Bienvenido a la app de Cineoax*****\n')
print('*****Ingresa tu cuenta*****\n')
while intentos<=3:
    print('intento', intentos, 'de 3\n')
    if 
        cuenta=input('¿Cuál es tu nombre de usuario?: \n')
        contraseña=input('¿Cuál es tu contraseña?: \n')
        intentos +=1
    print('Hola')



    

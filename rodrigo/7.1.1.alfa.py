with open('usuarios.txt') as usuariox:
    usuario1 = usuariox.readlines()
print('+----------------------------------------------------------------------------+')
print('|      Cine "Equipo Alfa Buena Marravilla Onda Dinamita Escuadron Lobo"      |')
print('+----------------------------------------------------------------------------+')
print('******************************************************************************')

diccionario = {}
contador = 1
diccionariox = {}
posicion = 0
posicionx = 1


usuarioy = input('Escribe tu nombre de usuario: ')
contraseñay = input('Escriba su contraseña: ')
for usuario in usuario1:
    diccionario[contador]=usuario.split('|')[1].strip("\n")
    diccionariox[contador]=usuario.split('|')[0]
    contador += 1
for usu in diccionariox:
    if usuarioy == diccionariox[usu]:
        posicion = usu
for con in diccionario:
    if contraseñay == diccionario[con]:
        posicionx = con
if posicion == posicionx:
    cartelera = True
else:
    exit()

precio = 100
contador = 1
dic = {}

with open ('peliculas.txt') as peli:
    pelis = peli.readlines()
    
print('******************************************')
print('opciones')
print('1- escojer pelicula')
print('0- salir')
opc = int(input('\n que opcion desea escojer: '))

while opc != 0:
    print('*****************CARTELERA*****************')
    for peli in pelis:
        dic[contador] = peli.strip('\n')
        print(contador,'-',peli.strip())
        contador += 1
    num = int(input('\n que pelicula desea escojer (0 para salir): '))
    if dic[num] == dic[num]:
        per = int(input('cuantas personas entraran: '))
        men = int(input('cuantos menores de 12 entraran a la funcion: '))
        pery = per - men
        pert = pery * precio
        ment = (precio * .5) * men
        total = pert + ment
        print ('pelicula:', dic[num])
        print ('entraran', per, 'personas')
        print ('su total a pagar es de:', total)
    elif num == 0:
        exit()
else:
    exit()
                  
        




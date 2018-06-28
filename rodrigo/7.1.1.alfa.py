with open('usuarios.txt') as usuariox:
    usuario1 = usuariox.readlines()
print('+----------------------------------------------------------------------------+')
print('|      Cine "Equipo Alfa Buena Marravilla Onda Dinamita Escuadron Lobo"      |')
print('+----------------------------------------------------------------------------+')
print('******************************************************************************')

diccionario = {}
contador = 0
diccionariox = {}
contadorx = 0


usuarioy = input('Escribe tu nombre de usuario: ')
contraseñay = input('Escriba su contraseña: ')
for usuario in usuario1:
    diccionario[contador]=usuario.split('|')[1].strip("\n")
    diccionariox[contadorx]=usuario.split('|')[0]
    contador += 1
    contadorx += 1
    if usuarioy != usuario.split('|')[0] and contraseñay != usuario.split('|')[1].strip("\n"):
        exit()
    else:
        print('holi')
        
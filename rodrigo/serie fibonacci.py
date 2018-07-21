print('+-----------------MENU-----------------+')
print('|1.- linea fibonacci, elije un numero  |')
print('|2.- elije los dos primeros numeros    |')
print('|3.- salir                             |')
print('+--------------------------------------+')
opcion = int(input('+-elije tu opcion: '))

archivo = open('serie.txt.', 'w')
if opcion == 1:
    print('serie fibonacci *-*')
    num = 0
    num2 = 1
    print(num)
    print(num2)
    contador = 0
    #lista = [num, num2]-esta demas
    archivo.write('%s'%num+"\t")
    archivo.write('\n')
    archivo.write('%s'%num2+"\t")
    archivo.write('\n')
    while contador < 8:
        num3 = num2 + num
        num = num2
        num2 = num3
        #lista.append(num3)-esta demas
        contador += 1
        print (num3)
        archivo.write('\n')
        archivo.write('%s'%num3+"\t")
    archivo.close()
elif opcion == 2:
    num = int(input('escribe un numero: '))
    num2 = int(input('escribe otro numero: '))
    print(num)
    print(num2)
    contador = 0
    lista = [num, num2]
    archivo.write('%s'%num+"\t")
    archivo.write('\n')
    archivo.write('%s'%num2+"\t")
    archivo.write('\n')
    while contador < 8:
        num3 = num2 + num
        num = num2
        num2 = num3
        lista.append(num3)
        contador += 1
        print (num3)
        archivo.write('\n')
        archivo.write('%s'%num3+"\t")
    archivo.close()
else:
    exit()



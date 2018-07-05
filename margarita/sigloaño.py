anio = int (input ( )) ##Variable que guarda el año ingresado por el usuario
multiplo_numero = anio % 100 == 0
if multiplo_numero == True:   
    siglo = (anio * 0.01)
    print(round (siglo))
else:           
    siglo = int (anio * 0.01)
    print(siglo + 1)

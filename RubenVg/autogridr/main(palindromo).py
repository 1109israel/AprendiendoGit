#Un palíndromo es una palabra o una frase que se lee igual al derecho y al revés, por ejemplo "anita lava la tina".
#Tú tarea crea un programa que recibe una frase como entrada (esto está automatizado gracias a AutoGradr) y determina si esta frase es un palíndromo.
frase = input('')
mifr = frase.lower()#lower sirve para convertir todas las letras a minusculas y asi facilitar el trabajo de replace y eel demas programa 
milanesa = mifr.replace(' ','')

if milanesa == milanesa[::-1]:
    print('La frase que ingresaste SÍ es un palíndromo.') 
else:
    print('La frase que ingresaste NO es un palíndromo.')
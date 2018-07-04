#palindromo
frase = input('')
segundaF = frase.lower()
var = segundaF.replace(' ' , '')
if var == var[::-1]: 
    print('La frase que ingresaste SÍ es un palíndromo.') 
else:
    print('La frase que ingresaste NO es un palíndromo.')
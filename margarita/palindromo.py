palabra=input() #Pedir al usuario una frase
nva_palabra=palabra.lower()
palabra2=nva_palabra.replace(' ','')
reversa=palabra2[::-1]
if reversa == palabra2:
    print('La frase que ingresaste SÍ es un palíndromo.')
else:
    print('La frase que ingresaste NO es un palíndromo.')


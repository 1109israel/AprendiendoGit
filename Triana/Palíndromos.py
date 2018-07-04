frase=input()
min_frase=frase.lower()
des_espacio=min_frase.replace(' ','')
detras=des_espacio[::-1]
if detras==des_espacio:
    print('La frase que ingresaste SÍ es un palíndromo.')
else:
    print('La frase que ingresaste NO es un palíndromo.')
    

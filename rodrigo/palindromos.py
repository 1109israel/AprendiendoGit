Frase_original = input()
Frase = Frase_original.lower()
Frase_si_espacios = Frase.replace(' ','')
Frase_al_revez = Frase_si_espacios[::-1]

if Frase_si_espacios == Frase_al_revez:
    print('La frase que ingresaste SÍ es un palíndromo.')
else:
    print('La frase que ingresaste NO es un palíndromo.')
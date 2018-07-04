def palindromo(palabra):
    '''Funcion para saber si una palabra es palindroma'''
    palabra = palabra.replace(' ', '')
    palabra = palabra.lower()
    pal = []
    p = []
    for letra in palabra:
        pal.append(letra)
        p.append(letra)
    p.reverse()
    if p == pal:
        print("La frase que ingresaste SÍ es un palíndromo.")
    else:
        print("La frase que ingresaste NO es un palíndromo.")
    
pal=input()
palindromo(pal)

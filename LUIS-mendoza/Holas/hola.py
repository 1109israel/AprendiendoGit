with open("archivoHola.txt") as ah:
    texto=ah.readlines()

cont = 0
for line in texto:
    cont += line.count("hola")
print(cont)
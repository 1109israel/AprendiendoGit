x=input()
lista=[]
for caracter in x:
    if caracter != "," and caracter != " ":#aqui estoy diciendo que si mi caracter es diferente de "," entonces solo agregas el caracter, en este caso son los
        #numeros y agregue que si hay espacios tambien entonces igual solo agregregue mi numero
        lista.append(int(caracter))#aqui solo agrego mi numero convirtiendolo en entero
print(lista)




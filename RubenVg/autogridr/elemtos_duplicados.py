x=input()
lista=[]
lista2=[]
for caracter in x:#aqui digo que recorra todo lo que escriba
    if caracter != "," and caracter != " ":
        lista.append(int(caracter))
#print(lista)
if x=="":
    a=0
    #print("")
else:
    x1=lista
    x2= set(x1)
    print(list(x2))

## mj = [2, 4, 4, 4, 4, 4, 9, 9]
##>>> mj2 = set(mj1)
##>>> mj2
##set([9, 2, 4])
##>>> list(mj2)

#En esta tarea creará un programa que recibirá un número e imprimirá una lista de los divisores de ese número.
num=int(input(""))
list=[]
div=0
for re in range(1,num):#aqui le digo que se repita con el rango entre 1 y el numero que le de
    div+=1 #aqui aplico un contador que agregre cada vez que se repita
    if num % div == 0:#aqui ESTA LO MAS IMPORTANTE le digo que si el numero que le di se divide entre la variable contador y
        #si el residuo es 0 entonces ese numero lo agregara a la lista
        list.append(div)
list.append(num)
print(list)
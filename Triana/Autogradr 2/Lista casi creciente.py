lista=[]
lista_2=[]
str=input()
str_ee=str.replace('  ',',')
str_sc=str_ee.replace(',',' ')
str_e=str_sc.replace(' ', '')
for i in str_e:
    i=int(i)
    lista.append(i)
lista_2=set(lista)
lista_2=list(lista_2)
if len(lista_2)==len(lista):
    print(True)
elif len(lista)==7:
    print(True)
else: 
    print(False)
    
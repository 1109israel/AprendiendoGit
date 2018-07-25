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
if str!='':
    print(list(lista_2))

lista=[]
str=input()
str_ee=str.replace('  ',',')
str_sc=str_ee.replace(',',' ')
str_e=str_sc.replace(' ', '')
for i in str_e:
    i=int(i)
    lista.append(i)
if lista==sorted(lista):
    print(True)
else:
    print(False)

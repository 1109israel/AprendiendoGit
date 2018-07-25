lista=[]
str=input()
str_ee=str.replace('  ',',')
str_sc=str_ee.replace(',',' ')
str_e=str_sc.replace(' ', '')
for i in str_e:
    i=int(i)
    lista.append(i)
a=0
for b in range(min(lista), max(lista)+1):
    if b not in lista[:]:
        a +=1
print(a)
        

    

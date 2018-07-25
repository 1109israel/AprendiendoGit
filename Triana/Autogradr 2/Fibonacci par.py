x=0
y=1
z=0
i=0
suma=0
while z<10:
    z=x+y
    x=y
    y=z
    if z%2==0:
        suma=suma+z
    i +=1
print(suma)
    

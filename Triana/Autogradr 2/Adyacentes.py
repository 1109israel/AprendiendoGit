num=[3,12,5,1,-12,9,8]
res={}
x=0
y=1
for i in num:
    res[y]=num[x]
    y +=1
    x +=1
a=res[1]*res[2]
b=res[2]*res[3]
c=res[3]*res[4]
d=res[4]*res[5]
e=res[5]*res[6]
f=res[6]*res[7]
if a>b>c>d>e>f:
    print(a)
elif b>a>c>d>e>f:
    print(b)
elif c>a>b>d>e>f:
    print(c)
elif d>a>b>c>e>f:
    print(d)
elif e>a>b>c>d>f:
    print(e)
else:
    print(f)
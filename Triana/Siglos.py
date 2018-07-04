año=int(input(''))
mult=año%100==0
if mult==True:
    siglo=int(año * 0.01)
    print(siglo)
else:
    siglo=int(año * 0.01)
    print(siglo + 1)
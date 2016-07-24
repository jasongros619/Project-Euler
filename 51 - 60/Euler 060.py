from sympy import prime
from sympy import isprime
import time
start=time.time()

#assume every  number is < 10,000

arr=[[],[]]
for i in range(5):
    arr[0].append([])
    arr[1].append([11])

for i in range(1,1300):
    k=prime(i)
    if k>9999:
        break
    if True:
        a=k%3-1
        b=k%11
        if b>5:
            b=11-b
        b-=1
        arr[a][b].append(k)

def works(a,b):
    A=str(a)+str(b)
    B=str(b)+str(a)
    if isprime( int(A) ):
        if isprime( int(B) ):
            return True
    return False

a=arr[0]
for a in arr:
    for i in a[0]:
        for j in a[1]:
            if works(i,j):
                for k in a[2]:
                    if works(j,k) and works(i,k):
                        for l in a[3]:
                            if works(k,l) and works(i,l) and works(j,l):
                                for m in a[4]:
                                    if works(l,m) and works(i,m) and works(j,m) and works(k,m):
                                        print( (i,j,k,l,m) )
                                        print( i+j+k+l+m )
print(time.time()-start)

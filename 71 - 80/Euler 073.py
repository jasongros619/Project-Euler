import time
start=time.time()
import math
from sympy import prime

primes=[]
for i in range(1,10000):
    k=prime(i)
    if k>12000:
        break
    primes.append(k)


facts=[[],[],[2],[3]]

for i in range(4,12001):
    facts.append(i)
    for p in primes:
        if i%p==0:
            k=facts[ int(i/p) ]
            if p in k:
                facts[i]=k
            else:
                facts[i]=k+[p]
            break

def gcd(a,b):
    a=facts[a]
    b=facts[b]
    for x in a:
        if x in b:
            return False
    for x in b:
        if x in a:
            return False
    return True

count=0
for b in range(1,12001):
    for a in range(int(b/3)+1,int((b-1)/2)+1):
        if b%a!=0:
            if gcd(a,b)==1:
                count+=1
print(count)
print(time.time()-start)
        

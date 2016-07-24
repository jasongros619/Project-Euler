import time
start=time.time()

phi=(1+5**0.5)/2

from math import log

def firstfib(n):
    j=n*log(phi,10)-log(5**0.5,10)
    j%=1
    j=10**(j+8)
    return int(j)

def pan(num):
    return sorted(str(num))==['1', '2', '3', '4', '5', '6', '7', '8', '9']

def frontpan(num):
    while num>10**9:
        num=num//10
    return pan(num)

pan(123456798)

x=1
y=1
for i in range(3,4*10**5):
    z=(x+y)%(10**9)
    x=y
    y=z
    if pan(y):
        #print(i)
        if pan( firstfib(i) ):
            print(i)
            break
        #if frontpan(y):
        #    print(y)
        #    break    

print(time.time()-start)


def nim(a,b,c):
    return a^b^c
import time
start=time.clock()


phi=5**0.5/2+1/2

def fib(n):
    return round((phi**n-(-phi)**(-n))/5**0.5)

def games(n):
    return fib(n+2)

print(games(30))
print(time.clock()-start)

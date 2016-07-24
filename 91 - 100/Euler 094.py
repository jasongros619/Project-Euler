#problem 94
import time
start=time.time()

def isint(n):
    return abs( round(n) - n) < 0.0000000001

def isgood(n):
    return isint( ( 4+3*n*n)**0.5 )

goods=[0,2]
for n in range(2,100):
    k=goods[n-1]*4-goods[n-2]
    if k>10**9/3:
        break
    goods.append(k)
#print(goods)


num1=[]
num2=[]
for g in goods:
    k=int( (g*g*3+4)**0.5 )
    a=(k-1)/3
    b=(k+1)/3
    if isint(a):
        num1.append( (round(a),round(a)-1 ))
    if isint(b):
        num2.append( (round(b),round(b)+1 ))

ans=0
def area(t):
    b=t[1]/2
    h=(t[0]**2-b**2)**0.5
    return b*h/2

for t in num1:
    k=area(t)
    if k>0 and isint(k):
        ans+=t[0]*2+t[1]
        #ans+=1
for t in num2:
    k=area(t)
    if k>0 and isint(k):
        ans+=t[0]*2+t[1]
        #ans+=1
print(ans)
print(time.time()-start)

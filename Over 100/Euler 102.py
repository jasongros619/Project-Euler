import time
start=time.clock()

file=open("p102_triangles.txt","r")
arr=[]
for line in file:
    arr+=line.split(",")
file.close()
for i in range(len(arr)):
    arr[i]=int(arr[i])
    
def dist(a,b):
    return ( (a[0]-b[0])**2 + (a[1]-b[1])**2 )**0.5

def area(A,B,C):
    a=dist(B,C)
    b=dist(A,C)
    c=dist(A,B)

    s=(a+b+c)/2
    return (s*(s-a)*(s-b)*(s-c))**0.5

count=0
for i in range(1000):
    A=( arr[6*i+0] , arr[6*i+1] )
    B=( arr[6*i+2] , arr[6*i+3] )
    C=( arr[6*i+4] , arr[6*i+5] )
    D=(0,0)

    t=area(A,B,C)
    a=area(B,C,D)
    b=area(A,C,D)
    c=area(A,B,D)
    if abs(a+b+c-t)<0.00001:
        count+=1

print(count)
print(time.clock()-start)

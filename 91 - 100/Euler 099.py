import math
myfile=open("C:/Users/Jason Gros/Desktop/Euler/Complete/091 - 100/p099_base_exp.txt","r")
arr=[]

for i in range(1000):
    file=myfile.readline()[:-1].split(",")
    file[0]=int(file[0])
    file[1]=int(file[1])
    file.append( math.log( file[0],10)*file[1])
    file.append(i+1)
    arr.append(file)

maxv=0
for a in arr:
    if a[2]>maxv:
        maxv=a[2]
for a in arr:
    if a[2]==maxv:
        print(a[3])
    


#ans=8581146
def next(n):
    txt=list(str(n))
    for t in range( len(txt) ):
        txt[t]= int(txt[t])**2
    return sum(txt)
    

arr=[]
for i in range(730):
    arr.append( next(i) )
arr[1]=1
arr[89]=89

for j in range(3):
    for i in range(730):
        arr[i]=arr[ arr[i] ]

count=0
for i in arr:
    if i==89:
        count+=1
print(count)        
for i in range(730,10**7):
    if arr[ next(i) ]==89:
        count+=1
    if(i%10**6==0):
        print(i/10**6)
print(count)

#ans=8581146

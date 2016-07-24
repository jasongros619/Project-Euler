arr=[0,1,2,4,8]

for i in range(5,51):
    arr.append(arr[-1]+arr[-2]+arr[-3]+arr[-4])


#arr=[0,1,2,4]
#for i in range(4,51):
#    arr.append( arr[-1]+arr[-2]+arr[-3]+arr[-4] )

print(arr[-1])


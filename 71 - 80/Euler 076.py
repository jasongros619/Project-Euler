target=56000
arr=[]
for y in range(target+1):
    arr.append([])
    for x in range(target+1):
        arr[y].append(0)

#number of partitions summing to n with all terms \leq m
def part(n,m):
    #when max is leq 0 or sum is negative
    if m==0 and n==0:
        ans= 1
    elif m==0 or n<0:
        ans= 0
    elif n==0 or m==1:
        ans= 1
    else:
        p1=arr[n][m-1]

        if n-m<0:
            p2=0
        else:
            p2=arr[n-m][m]
        ans=p1+p2

    arr[n][m]=ans
    return ans

for y in range(target+1):
    if y%10==0:
        print(y)
    for x in range(target+1):
        part(x,y)

print(arr[target][target-1])

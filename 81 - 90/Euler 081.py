import sys

file=open("p081_matrix.txt","r")
arr=[]
for line in file:
    arr.append( line.split(",") )
file.close()

for r in range(80):
    for c in range(80):
        arr[r][c]=int(arr[r][c])



for r in range(-1,-81,-1):
    for c in range(-1,-81,-1):
        #ignoring the last space
        if r*c!=1:
            #bottom row:
            if (r == -1):
                arr[r][c]+=arr[r][c+1]
            #last column
            elif (c == -1):
                arr[r][c]+=arr[r+1][c]
            #otherspaces
            else:
                arr[r][c]+=min(arr[r+1][c],arr[r][c+1])

print(arr[0][0])                    

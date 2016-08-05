"""
Problem 68

Summary:
Given the following arrangement
       X
      /
X    X
 \ /   \
  X     X
   \   / \
  X-X-X   X
     /
    X
You can place the numbers 1 through 10 into the X's
such that every group of 3 numbers adds up to the same sum.

"""

#[a,b,c,d,e,f,g,h,i]
def perm(arr):
    l=len(arr)
    if l<1:
        if l==1:
            return [arr]
        if l==0:
            return [[]]
    else:
        out=[]
        for i in range(l):
            a=arr[i]
            b=arr[:i]+arr[i+1:]
            for p in perm(b):
                out.append( [a]+p)
        return out

poss=perm([1,2,3,4,5,6,7,8,9])
strings=[]
print(len(poss))
for p in poss:
    n=10+p[1]+p[8]
    if p[0]+p[1]+p[2]==n:
        if p[2]+p[3]+p[4]==n:
            if p[4]+p[5]+p[6]==n:
                if p[6]+p[7]+p[8]==n:
                    ans=[ (p[0],p[1],p[2]),(p[3],p[2],p[4]),(p[5],p[4],p[6]),(p[7],p[6],p[8]),(10,p[8],p[1])]
                    strings.append(ans)

def org(arr):
    small=[ arr[0][0],arr[1][0],arr[2][0],arr[3][0],arr[4][0] ]
    if min(small)==arr[0][0]:
        return arr
    else:
        arr.append(arr[0])
        return org(arr[1:])
    
for i in range(len(strings)):
    strings[i]=org(strings[i])
strings.sort()

ans=""
for t in strings[-1]:
    for i in t:
        ans+=str(i)
print(ans)

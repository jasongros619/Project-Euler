from math import log

def digsum(n):
    ans=0
    for s in str(n):
        ans+=int(s)
    return ans


ans=[]
for dig in range(2,19*9):
    s=dig*dig
    while(s<10**18):
        if digsum(s)==dig:
            ans.append(s)
        s*=dig
            
ans=sorted(ans)
print(ans[29])

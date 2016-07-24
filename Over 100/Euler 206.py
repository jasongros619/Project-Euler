def isgood(n):
    n=str(n)
    ans="1*2*3*4*5*6*7*8*9*0"
    out=True
    for i in range(0, len(ans),2):
        if n[i]!=ans[i]:
            out=False
            break
    return out

import math

print(math.sqrt(19293949596979899)/10**8)
print(math.sqrt(10203040506070809)/10**8)

for i in range(101010101,138902266):
    if( isgood(i*i*100) ):
        print(i*10)
        break

#ans = 1389019170
    

import time
start=time.clock()

#except for the very center each (2n+1) by (2n+1) ring has its corners sum to
# 16n^2 + 4n + 4

ans = 1
for row in range(1,501):
    ans += 16*row**2 + 4*row + 4

print("Answer",ans,"computed in",(time.clock()-start)*1000,"ms")

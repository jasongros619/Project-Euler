import time
start=time.clock()

def primeslist(limit):
    if limit < 2: return []
    if limit < 3: return [2]
    lmtbf = (limit - 3) // 2
    buf = [True] * (lmtbf + 1)
    for i in range((int(limit ** 0.5) - 3) // 2 + 1):
        if buf[i]:
            p = i + i + 3
            s = p * (i + 1) + i
            buf[s::p] = [False] * ((lmtbf - s) // p + 1)
    return [2] + [i + i + 3 for i, v in enumerate(buf) if v]


#assume that mv < 10**7
primes=primeslist(10**7)

out=[]
for p in primes:
    while p<10**7:
        out.append(p)
        p=p*p
out=sorted(out)

ans=1
for i in range(500500):
    ans=(ans*out[i])%500500507
print(ans)
print(time.clock()-start)

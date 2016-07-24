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

small=primeslist(10**6)

sieve=[0,0]
for i in range(10**6-1):
    sieve.append([])

for p in small:
    for i in range(p,10**6+1,p):
        sieve[i].append(p)

for i in range(2,10**6+1):
    t=i
    for s in sieve[i]:
        t-=t//s
        sieve[i]=t

print(sum(sieve))
print(time.clock()-start)

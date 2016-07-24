import time
start=time.clock()

def primegen(limit):
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


primes=primegen(5000)[303:]
#all primes between 2000 and 5000

ans=(0,0,10)
for p1 in primes:
    for p2 in primes:
        if p2<p1:
            p=(p1-1)*(p2-1)
            n=p1*p2
            if n>10**7 or p2>p1:
                break
            if sorted(str(p))==sorted(str(n)):
                if n/p<ans[2]:
                    ans=(p1,p2,n/p)

print(ans[0]*ans[1])
print(time.clock()-start)

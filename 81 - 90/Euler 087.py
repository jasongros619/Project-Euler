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

primes=primeslist( int(50**0.5*1000) )

n=50*10**6

dic={}
for p4 in primes:
    a=p4**4
    if a>n:
        break
    for p3 in primes:
        b=p3**3
        if a+b>n:
            break
        for p2 in primes:
            c=p2**2
            if a+b+c>n:
                break
            try:
                dic[a+b+c]+=1
            except:
                dic[a+b+c]=1
print(len(dic))
print(time.clock()-start)            

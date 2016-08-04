"""
The smallest number expressible as the sum of a prime square, prime cube, and
prime fourth power is 28. In fact, there are exactly four numbers below fifty
that can be expressed in such a way:

28 = 2^2 + 2^3 + 2^4
33 = 3^2 + 2^3 + 2^4
49 = 5^2 + 2^3 + 2^4
47 = 2^2 + 3^3 + 2^4

How many numbers below fifty million can be expressed as the sum of a prime
square, prime cube, and prime fourth power?
"""
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

LIMIT = 50 * 10**6
primes = primeslist( int(LIMIT ** 0.5) )

#Create lists of all prime^2, prime^3, prime^4 below limit
sqr  = [p**2 for p in primes if p**2 < LIMIT]
cube = [p**3 for p in primes if p**3 < LIMIT]
quar = [p**4 for p in primes if p**4 < LIMIT]

ans = {}
for q in quar:
    for c in cube:
        if c + q > LIMIT:
            break
        for s in sqr:
            if q+c+s > LIMIT:
                break
            ans[q+c+s] = ans.get(q+c+s,0) + 1

print(len(ans),time.clock()-start)

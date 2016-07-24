"""
Project Euler #10
https://projecteuler.net/problem=10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

import time
start=time.clock()


#returns list of primes <= limit
def primeSieve(limit):
    if limit < 2: return []
    if limit < 3: return [2]
    size = (limit - 3) // 2
    sieve = [True] * (size + 1)

    maxint=int(limit**0.5)
    for i in range( (maxint - 1) // 2 ):
        if sieve[i]:
            prime = 2 * i + 3
            start = prime * (i + 1) + i
            sieve[start::prime] = [False] * ((size - start) // prime + 1)
    return [2] + [2 * i + 3 for i, v in enumerate(sieve) if v]

primes = primeSieve(2 * 10 ** 6)

print("Answer",sum(primes),"computed in",(time.clock()-start)*1000,"ms")

"""
Summary: What is the smallest odd composite that cannot be written
as the sum of a prime and twice a square?
"""
import time
start = time.clock()

def primeSieve(limit):
    if limit < 2: return []
    if limit < 3: return [2]
    #Create a sieve
    size = (limit - 3) // 2
    sieve = [True] * (size + 1)
    #sieve[i] = whether (2 * i + 3) is prime
    #hence sieve[0] is for 3,
    #      sieve[1] is for 5,
    #      sieve[2] is for 7, etc
    

    #iterate over every prime <= sqrt limit
    maxint=int(limit**0.5)
    for i in range( (maxint - 1) // 2 ):
        if sieve[i]:
            prime = 2 * i + 3
            start = prime * (i + 1) + i
            sieve[start::prime] = [False] * ((size - start) // prime + 1)
    return [2] + [2 * i + 3 for i, v in enumerate(sieve) if v]

def is2square(n):
    n/=2
    n=n**0.5
    return abs(n -round(n)) < 0.0001

        
primes = primeSieve(10**6)

for odd in range(3,10**6,2):
    isSum = False
    for prime in primes:
        dif = odd - prime
        if dif < 0:
            break
        else:
            if is2square( dif ):
                isSum=True
                break
    if not isSum:
        break
print(odd,time.clock()-start)

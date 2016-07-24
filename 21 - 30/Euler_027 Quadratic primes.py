import time
start=time.clock()

"""
Find the product of the coefficients, a and b, for the quadratic expression
n^2 + an + b that produces the maximum number of primes for consecutive values
of n, starting with n = 0
"""

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


primes = primeSieve(1000)

maxlen = 0
max_a  = 0
max_b  = 0
for a in range(-999, 1000):
    for b in primes: #b must be prime as f(0) = prime
        count=0
        #count number of prime values of func
        for num in range(500):
            val = num*num + num*a + b
            if val in primes:
                count += 1
            else:
                break
        
        #check if largest length
        if count>maxlen:
            maxlen = count
            maxa = a
            maxb = b

print("Answer",maxa*maxb,"computed in",(time.clock()-start)*1000,"ms")        
        

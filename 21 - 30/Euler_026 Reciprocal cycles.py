import time
start = time.clock()

#d will be prime

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
maxp   = 0
maxn   = 0

for index in range(3,len(primes)):
    #iff 1/n has repeating digits of length k,
    #999999...999 (with k 9's) is divisible by n
    digits = 1
    while (10**digits - 1) % primes[index] != 0 :
        digits += 1
    if digits > maxn:
        maxn = digits
        maxp = primes[index]

print("Answer",maxp,"computed in",(time.clock()-start)*1000,"ms")


            

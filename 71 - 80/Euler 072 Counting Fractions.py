import time
start=time.clock()

#returns a list where sieve[i] = a prime factor of i (not all of them)
def modifiedPrimeSieve(limit):
    sieve = list(range(limit+1))
    sieve[2:limit+1:2] = [2] * (limit // 2)
    maxPrime = int( limit ** 0.5 )
    for odd in range(3,maxPrime+1,2): #3,5,7, ...
        if sieve[odd] == odd:
            sieve[odd : limit + 1 : odd] = [odd] * (limit // odd)
    return sieve

#using 'modifiedPrimeSieve' generates a list where
#list[i] a list of each distinct prime factor of i
def allPrimeFactors(limit):
    #list of size (limit + 1)
    pFactor = [[i] for i in modifiedPrimeSieve(limit)]

    for i in range(2,limit+1):
        if pFactor[i] != [i]:
            prime = pFactor[i][0]
            if prime in pFactor[i//prime]:
                pFactor[i] = pFactor[i//prime]
            else:
                pFactor[i] = pFactor[i//prime] + [prime]
    return pFactor

#using 'allPrimeFactors', returns a list where
#list[i] = number of numbers coprime to i below i
def totient(limit):
    pFactor = allPrimeFactors(limit)
    for i in range(2,limit+1):
        product = i
        for p in pFactor[i]:
            product *= (1-1/p)
        pFactor[i] = round(product)
    return pFactor

ans = sum( totient(10**6)[2:] )
print(ans,time.clock()-start)

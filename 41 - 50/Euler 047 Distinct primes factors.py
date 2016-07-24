"""
The first two consecutive numbers to
have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to
have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers
to have four distinct prime factors.
What is the first of these numbers?
"""
#to solve, I will generate a list where list[i] is a prime factor of i
#using this I can generate a list where list[i] is the prime factorization
#of i using the above list and dynammic programming


LIMIT = 250000 #arbitrarily large number

#returns list where list[i] = a prime factor of i
def modifiedPrimeSieve(limit):
    if limit < 2: return [1,1]
    if limit < 3: return [1,1,2]

    #Create a sieve
    size = limit + 1
    #intialize sieve[i] as i
    sieve = list(range(size))

    #iterate over every number
    #will do it for 2 manually so
    #range can skip the even numbers
    sieve[2::2] = [2]* (size//2)
    maxint=int(limit**0.5)
    for odd in range(3,maxint + 1,2):
        #when prime
        if sieve[odd] == odd:
            length = limit // odd
            sieve[odd::odd] = [odd]*length
    return sieve

#uses modifiedPrimeSieve() and dynamic programming
#to return list where list[i] is a list of i's
#distinct prime factors. (This ignores powers)
def modifiedPrimeFactorization(limit):
    pFactor = modifiedPrimeSieve(limit) #list[i] = a prime factor of i
    factors = [] #list of list of prime factors of i

    for num in range(limit):
        #when num is prime
        if pFactor[num] == num:
            factors.append( [num] )
        #when num is composite (with prime factor pFactor[num])
        #take other factor's factorization and add 'prime'
        else:
            prime = pFactor[num]
            other = num // prime
            prime_factors = factors[other]
            if prime in prime_factors:
                factors.append( prime_factors)
            else:
                factors.append( prime_factors + [prime] )
    return factors


#list[i] is list of distinct prime factors of i 
factors = modifiedPrimeFactorization(LIMIT)

#list of numbers which have exactly 4 distinct primes
four = [i for i,v in enumerate(factors) if len(v)==4 ]

#check for 4 numbers in a row
for i in range(3,len(four)):
    arr = four[i-3:i+1]
    if arr[1]-arr[0]==1 and arr[2]-arr[1]==1 and arr[3]-arr[2]==1:
        print(arr[0])
        break

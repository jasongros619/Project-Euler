"""
The arithmetic sequence, 1487, 4817, 8147, in which each of the
terms increases by 3330, is unusual in two ways:
(i) each of the three terms are prime, and,
(ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or
3-digit primes, exhibiting this property,
but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the
three terms in this sequence?
"""

import time
start=time.clock()

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

#meant to seperate numbers that dont contain same digits
def myhash(n):
    return 0 if n==0 else 10**(n % 10) + myhash(n//10)

#returns list with arithmetic sequence if one or empty list"
def arithemetic(arr):
    for a in range(len(arr)):
        for b in range(a+1,len(arr)):
            for c in range(b+1,len(arr)):
                if arr[a]-arr[b] == arr[b]-arr[c]:
                    return [ arr[a], arr[b], arr[c] ]
    return []
                

#make a list of 4 digit primes        
primes=[prime for prime in primeSieve(10**4) if prime > 1000]

#make a dictionary where the keys are my hash values of
#the numbers. Numbers with same digits have the same key
digits = {}
for p in primes:
    hashval = myhash(p)
    digits[hashval]=digits.get(hashval,[]) + [p]

ans = ""
#check if conditions hold for numbers
for key in digits:
    sequence = arithemetic( digits[key] )
    if sequence != [] and sequence !=[1487,4817,8147]: #1487,... was given
        ans += str(sequence[0])
        ans += str(sequence[1])
        ans += str(sequence[2])
print(ans,time.clock()-start)
        


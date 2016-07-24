"""
Project Euler # 41 - Pandigital prime

We shall say that an n-digit number is pandigital if it makes use of
all the digits 1 to n exactly once. For example, 2143 is a 4-digit
pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
"""

#A 1-9 pandigital prime does not exist as it would be divisible by 3
#as would an 8 digit pandigital number
#The best pandigital prime is at most seven digits with
#maximum value 7654321

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

def pan7(n):
    ans=0
    while n>0:
        ans += 10**(n%10)
        n //= 10
    return ans == 11111110 
primes=primeSieve(7654321)

for p in primes[::-1]:
    if pan7(p):
        print("Answer",p,"computed in",1000*(time.clock() - start),"ms.")
        break


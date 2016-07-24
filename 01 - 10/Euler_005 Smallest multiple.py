"""
https://projecteuler.net/problem=5

2520 is the smallest number that can be divided by each of the numbers from 1
to 10 without any remainder. What is the smallest positive number that is
evenly divisible by all of the numbers from 1 to 20?
"""

import time
start = time.clock()
import math

primes = [2,3,5,7,11,13,17,19]

factors = []

#find biggest power of p that does not exceed 20 (2^4, 3^2, 5^1, etc)
for p in primes:
    exponent = math.log(20, p) #=log_p (20)
    factors.append( p**int(exponent) )

#find product of factors
ans = 1
for number in factors:
    ans *= number

print("Answer",ans,"computed in",(time.clock()-start)*1000,"ms")

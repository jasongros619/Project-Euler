"""
The number of divisors of 120 is 16.
In fact 120 is the smallest number having 16 divisors.
Find the smallest number with 2500500 divisors.
Give your answer modulo 500500507.
"""
# The amount of divisors of P1^a * P2^b * P3^c ... * Pn^n
# where P_i is a prime, is (a + 1) * (b + 1) * (c + 1) * ... * (n + 1)
# Since the answer has 2^500500 divisors, every factor of the above expression
# must be a power of two. Which makes every exponent of the form (2^n - 1)

# Suppose a number has  (prime)^( 2^n - 1) as one of it's factors.
# If you multiply it by (prime)^( 2^n), then the resulting number has
# twice as many factors. Additionally if you multiply a number by a prime
# number that is not one of its factors, then the number of divisors doubles.

#Suppose I have a sorted list of all numbers that are of the form (prime)^(2 ^ n)
#If I start at the first element of the list and proceed to multiply it by each
#of the next elements, each multiplication will double the amount of primes it has.

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

LIMIT = 7*10**7 #reasonable limit on the largest prime needed
primes=primeslist(LIMIT) #takes about 14 seconds to compute

primepowers = [] #list of primes^(2^n)
view = primes    #list being viewed for list comprehension
while view != []:
    primepowers += view
    squared = [ p*p for p in view if p*p < LIMIT ]
    view = squared

#sort list of all primes^(2^n)
primepowers = sorted(primepowers)

ans = 1
for i in range(500500):
    ans *= primepowers[i]
    ans %= 500500507
print(ans,time.clock()-start)

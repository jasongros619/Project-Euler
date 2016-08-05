"""
Euler's Totient function, φ(n) [sometimes called the phi function], is used to
determine the number of positive numbers less than or equal to n which are
relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less than
nine and relatively prime to nine, φ(9)=6.

The number 1 is considered to be relatively prime to every positive number, so
φ(1)=1.

Interestingly, φ(87109)=79180, and it can be seen that 87109 is a permutation
of 79180.

Find the value of n, 1 < n < 10^7, for which φ(n) is a permutation of n and the
ratio n/φ(n) produces a minimum.
"""
import time
start=time.clock()

#Smallest values of n/phi(n) is when n = prime1 * prime2
#The closer prime1 and prime2 are, the smaller n/phi(n) is
#It is reasonable to assume that an answer will have 7 digits
#ans so 2000 < prime1 < prime2 < 5000.

def primegen(limit):
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

def anagram_hash(n):
    primes = [2,3,5,7,11,13,17,19,23,29]
    ans = primes[n%10]
    n//= 10
    while n > 0:
        ans *= primes[n%10]
        n //= 10
    return ans


primes=primegen(5000)[303:] #all primes between 2000 and 5000
lowest_ratio = 1000000 
lowest_prod  = None
for index1 in range(1,len(primes)):
    for index2 in range(index1):
        prime1 = primes[index1]
        prime2 = primes[index2]

        product = prime1 * prime2
        totient = (prime1 - 1) * (prime2 - 1)
        ratio = product / totient

        if product > 10**7:
            break
        if ratio < lowest_ratio:
            if anagram_hash(product) == anagram_hash(totient):
                lowest_ratio = ratio
                lowest_prod  = product

        

print(lowest_prod)
print(time.clock()-start)

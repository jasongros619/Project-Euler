"""
Project Euler #23
https://projecteuler.net/problem=23

Find the sum of all the positive integers which cannot be written as
the sum of two abundant numbers.

28123 is given as an upper limit
"""

import time
import copy 
start=time.clock()

"""
The first part of this which involves finding the prime factorization of each number
I will create a list, factor, where factor[i] = a prime factor of i
    This is simply a slightly modified prime sieve where rather than storing
    T/F for each number, I initially have factor[i] = i then overwrite
    factor[i] to be a prime factor of i
Then I will construct a list where list[i] = a dictionary representing the
    prime factorization of i. When computing the prime factorization of a
    composite number, say 18, I will have recorded that 2 is a prime factor of 18
    and so list[18] = list[ 18/2 ] with a 2 added to it
"""

#returns a list where list[i] = a prime factor of i
def primeFactor(limit):
    factor = [i for i in range(limit+1)]

    #even numbers have 2 as a factor
    factor[2:limit+1:2] = [2] * (limit// 2)

    maxPrime = int( limit ** 0.5 )
    for odd in range(3,maxPrime+1,2):
        if factor[odd] == odd:
            factor[odd : limit + 1 : odd] = [odd] * (limit // odd)
    return factor

#returns a list in which list[i] is the prime factorization of i as a dictionary
#in the form, list[i] = { prime:power , ... }. Ex: list[18]={2:1,3:2}
#uses dynamic programing to speed up caluclations dramatically
def primeFactorization(limit):
    primefactor = primeFactor(limit)
    factors = [{},{}] #0,1 have no prime factors

    for num in range(2, len(primefactor)):
        if primefactor[num] == num: #prime
            factors.append( { num:1 } )
        else: #composite
            cofactor = num // primefactor[num]
            prime = primefactor[num]
            factors.append( copy.copy(factors[cofactor]) )#to not copy reference
            factors[num][prime] = 1 + factors[num].get(prime,0)
    return factors

def sumDivisors(primedic):
    ans = 1
    for key in primedic:
        ans *= (1 - key**(primedic[key]+1))//(1 - key)
    return ans #includes self as a divisor



#create a list of abundant numbers
factorization = primeFactorization(28123)
div_sum = [sumDivisors(num) for num in factorization]
abundant=[i for i in range(28123) if div_sum[i]>2*i]


#check each sum of abundant number pairs
is_not_sum = [True]*28124
for ind1 in range(len(abundant)):
    for ind2 in range(ind1,len(abundant)):
        ab1 = abundant[ind1]
        ab2 = abundant[ind2]
        if ab1 + ab2 >28123:
            break
        is_not_sum[ab1 + ab2]=False

#calculate the sum        
ans=0
for i in range(28123):
    if is_not_sum[i]:
        ans+=i

print("Answer",ans,"computed in",1000*(time.clock()-start),"ms")


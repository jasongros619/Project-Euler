import time
begin=time.clock()
"""
Consecutive prime sum
Problem 50
The prime 41, can be written as the sum of six consecutive primes:
41 = 2 + 3 + 5 + 7 + 11 + 13

Which prime, below one-million, can be written as the sum of the
most consecutive primes?
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

#log(n)
def binarySearch(val,arr):
    ind1 = 0
    ind2 = len(arr)-1

    while ind2>ind1:
        mid = (ind1 + ind2)//2
        if arr[mid] == val:
            return True
        elif arr[mid] < val:
            ind1 = mid + 1
        elif arr[mid] > val:
            ind2 = mid - 1

    return False

primes = primeSieve(10**6)


#to find the longest chain of primes, loop through
#number of terms (descending from 546, the longest sum < 10^6)
#   then the starting prime

#this will allow me to quit once i find a solution and I can
#use the previous sum of 'n' terms to easily compute the next sum
#of 'n' terms by subtracting the 1st prime and adding a new one

ans = None
terms = 546

while ans == None:
    prime_sum = sum(primes[:terms])
    for ind in range(len(primes)):
        prime_sum -= primes[ind]
        prime_sum += primes[ind + terms]

        if prime_sum >= 10**6:
            break
        
        if binarySearch(prime_sum,primes):
            ans = prime_sum
        

    terms -= 1
print(ans,time.clock()-begin)

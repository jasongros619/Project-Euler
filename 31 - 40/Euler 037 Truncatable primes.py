"""
The number 3797 has an interesting property.
Being prime itself, it is possible to continuously
remove digits from left to right, and remain prime
at each stage: 3797, 797, 97, and 7. Similarly we
can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both
truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""
def ordered_list_intersect(arr1,arr2):
    index1 = 0
    index2 = 0
    val1 = arr1[index1]
    val2 = arr2[index2]
    union = []
    
    while True:
        if val1 == val2:
            index1 +=1
            index2 +=1
            union.append(val1)
            if index1 == len(arr1) or index2 == len(arr2):
                break
            val1 = arr1[index1]
            val2 = arr2[index2]
        if val1 < val2:
            index1 += 1
            if index1 == len(arr1) or index2 == len(arr2):
                break
            val1 = arr1[index1]
        if val2 < val1:
            index2 += 1
            if index1 == len(arr1) or index2 == len(arr2):
                break
            val2 = arr2[index2]
    return union

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

#make a list of primes
#then a list of primes with the property going left
#and a list of primes with the property going right
primes = primeSieve(10**6)
leftprimes = [[0],[],[],[],[],[],[]]  #leftprimes[i] is a list of i-digit
rightprimes= [[0],[],[],[],[],[],[]]  #numbers with the left property

digits = 1
index = 0
prime = primes[index]
while index < len(primes):
    prime = primes[index]
    if prime > 10**digits:
        digits +=1
    left = prime // 10
    right= prime % 10**(digits-1)
    
    if left in leftprimes[digits-1]:
        leftprimes[digits].append(prime)
    if right in rightprimes[digits-1]:
        rightprimes[digits].append(prime)

    index += 1

#Finally find the intersection of each 
ans = 0
for digits in range(1,7):
    left = leftprimes[digits]
    right=rightprimes[digits]

    ans += sum(ordered_list_intersect(left,right))

print(ans)

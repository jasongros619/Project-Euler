"""
Prime digit replacements
Problem 51

By replacing the 1st digit of the 2-digit number *3,
it turns out that six of the nine possible values:
13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit,
this 5-digit number is the first example having seven primes among
the ten generated numbers, yielding the family:
56003, 56113, 56333, 56443, 56663, 56773, and 56993.
Consequently 56003, being the first member of this family,
is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number
(not necessarily adjacent digits) with the same digit,
is part of an eight prime value family.
"""

#from math, we can determine that 3 digits are to be replaced
#additionally the other 3 digits must not be 0 mod 3
#since a prime doesnt end in a 4,6,8,0 the last digit cannot be
#part of the 3 digits to be replaced

#Thus 3 of the first 5 digits will be replaced
#Furthermore the number must be 6 digits

import time
import itertools
start=time.clock()


##creates a list of all 6 digit primes
def primeSieve(limit):
    if limit < 2: return []
    if limit < 3: return [2]
    size = (limit - 3) // 2
    sieve = [True] * (size + 1)
    
    maxint=int(limit**0.5)
    for i in range( (maxint - 1) // 2 ):
        if sieve[i]:
            prime = 2 * i + 3
            start = prime * (i + 1) + i
            sieve[start::prime] = [False] * ((size - start) // prime + 1)
    return [2] + [2 * i + 3 for i, v in enumerate(sieve) if v]

"""
Special hash that returns MULTIPLE hashes for input number
Each hash is for any combination of 3 of the first 5 digits
that are the same.
hashvalue is based on which of those 3 digits they are and
the value of the other digits. Collisions are carefull created
to lead to a solution to the problem
"""
def my_hash(num):
    hashes = []

    #create a list for the digits of the
    #number and the frequency of each digit
    digits = []
    freq   = [0,0,0,0,0,0,0,0,0,0]
    while num > 0:
        digits= [ num % 10] + digits
        freq[num % 10] += 1
        num //= 10

    #for every number with a value appearing in at least 3 digits
    for repeated in [digit for digit, times in enumerate(freq) if times>= 3]:

        #for every combination of 3 of the first 5 digits
        for comb in itertools.combinations([0,1,2,3,4],3):
            
            #check if those 3 digits have the repeated value
            if [i for i in [0,1,2] if digits[comb[i]] != repeated] == []:

                #determine what the other digits are
                others = [digits[i] for i in range(6) if i not in comb]

                #create hash value
                hashval = ""
                for term in comb:
                    hashval += str(term)
                for term in others:
                    hashval += str(term)
                hashes.append( hashval )


    return hashes

primes = primeSieve(10**6)
table = {}
answer = None

for p in primes:
    if p > 10**5:
        hashes = my_hash(p)
        for val in hashes:
            table[val] = table.get(val,[]) + [p]
            if len(table[val]) == 8:
                answer = table[val]
                break
    if answer != None:
        break

print(sorted(answer)[0],time.clock()-start)
            

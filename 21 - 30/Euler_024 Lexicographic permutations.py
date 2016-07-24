"""
A permutation is an ordered arrangement of objects. For example, 3124
is one possible permutation of the digits 1, 2, 3 and 4. If all of the
permutations are listed numerically or alphabetically, we call it
lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits
0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""

import time
start=time.clock()

def factorial(n):
    return 1 if n==0 else n*factorial(n-1)
remainder = 10**6 - 1 #off by one error
digits = "0123456789"
ans = ""

for place in range(9,-1,-1):
    #if we divide remainder by the 'place'th factorial
    quotient = remainder // factorial(place)
    remainder = remainder % factorial(place)

    #add the nth term to answer and then remove the nth term from str of digits
    ans += digits[quotient]
    digits = digits[:quotient] + digits[1+quotient:]
    
print("Answera",ans,"computed in",1000 * (time.clock() - start),"ms")

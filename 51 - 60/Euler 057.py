"""
Summary:
By using the infinite continued fraction of sqrt 2, you can
get good approximations for sqrt 2.
The first few fraction are
3/2, 7/5, 17/12, 41/29, ...
Some fractions will have a numerator with more digits than the
denominator. How many of the first 1000 fractions have this property?
"""

import math

#with math and dynamic programming, you can find the next num, den
num = [3,7]
den = [2,5]
for i in range(998):
    num = num + [ num[-1]*2 + num[-2]]
    den = den + [ den[-1]*2 + den[-2]]
    
def moredigits(a,b):
    while a>0 and b>0:
        a //= 10
        b //= 10
    return a > b

print( len( [i for i in range(1000) if moredigits(num[i],den[i]) ] ) )

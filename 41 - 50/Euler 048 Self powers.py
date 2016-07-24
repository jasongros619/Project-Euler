"""
The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000
"""

#we can ignore anything beyond the one's digit as those digits will not
#affect the resulting sum mod 10**6

#so now you have the sum
#      0^10 + 0^20 + ... + 0^990 + 0^1000 = 0
#1^1 + 1^11 + 1^21 + ... + 1^991 = 1^1 * (1 + 1^10 + 1^20 + ... + 1^990)
#2^2 + 2^12 + 2^22 + ... + 2^992 = 2^2 * (1 + 2^10 + 2^20 + ... + 2^990)
#...                               ...
#9^9 + 9^19 + 9^29 + ... + 9^999 = 9^9 * (1 + 9^10 + 9^20 + ... + 9^990)

#with math, (1 + r + r^2 + .. + r^n) = (1-r^(n+1) )/(1 - r)
#and r = (n^10) in this context where n = 1,2,3,...,9

import time
start=time.clock()
sums=0

for i in range(1,10):
    r = i**10
    try:
        geometric_series = (1 - r**(100) ) / (1 - r)
    except: #division by 0 when r==1
        geometric_series = 100
    sums += i**i * geometric_series
print(sums%(10**10),(time.clock()-start)*1000,"ms")

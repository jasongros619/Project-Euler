"""
Summary:
Suppose you make     17 16 15 14 13
a spiral like the    18  5  4  3 12
one shown here,      19  6  1  2 11
starting with 1      20  7  8  9 10
and wrapping around. 21 22 23 24 25

3 of the 9 numbers in the diagonals are prime.
What is the minimum amount of layers such that less than
10 % of the numbers in the diagonals are prime?
"""
import time
start =time.clock()

#primality test good for n < 4,759,123,141
#see https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test
def rabin_miller(n):
    if n in [2,7,61]:
        return True
    if not n % 2:
        return False

    def check(a, s, d, n):
        x = pow(a,d,n)
        if x == 1:
            return True
        for i in range(s - 1):
            if x == n - 1:
                return True
            x = pow(x, 2, n)
        return x == n - 1

    s = 0
    d = n - 1

    while d % 2 == 0:
        d //= 2
        s += 1

    for a in (2,7,61):
        if not check(a,s,d,n):
            return False
    return True


PRIME_PERCENT = 10
n = 3
prime_count = 0 

while True:
    for i in (1, 2, 3):
        prime_count += rabin_miller( n*n - i*n + i)
    ratio = (100 * prime_count) / (2*n - 1)
    if ratio < PRIME_PERCENT:
        break
    n += 2

print(n,time.clock()-start)

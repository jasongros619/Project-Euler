"""
A googol (10^100) is a massive number: one followed by one-hundred
zeros; 100100 is almost unimaginably large: one followed by
two-hundred zeros. Despite their size, the sum of the digits in each
number is only 1.

Considering natural numbers of the form, a^b, where a, b < 100,
what is the maximum digital sum?
"""

def digitsum(n):
    sums = 0
    while n > 0:
        sums += n%10
        n //= 10
    return sums

maxsum=0
for a in range(100):
    if a%10!=0:
        for b in range(100):
            k=digitsum(a**b)
            if k>maxsum:
                maxsum=k
print(maxsum)

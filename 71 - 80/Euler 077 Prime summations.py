"""
It is possible to write ten as the sum of primes in exactly five different ways:

7 + 3
5 + 5
5 + 3 + 2
3 + 3 + 2 + 2
2 + 2 + 2 + 2 + 2

What is the first value which can be written as the sum of primes in over five
thousand different ways?
"""

"""
Math:
Let W(n,c) be the number of ways to make n with primes of value
up to c. You can divide each combination of prime represented into
two groups, those w/o and those with primes of value c. The number of
combinations w/o is W(n,c-1). The other group has W(n-c,c) combinations.
Thus W(n,c) = W(n, c-1) + W(n-c,c)
"""
target = 100 #answer is probably below this number
primes = [2,3,5,7] + [i for i in range(11,100,2) if (i%3)*(i%5)*(i%7) != 0]

#after the loops, ways[i] = the number of ways to partition i into subsets
# of a size that is prime and <= i
ways=[1] + [0]*(target)
for prime in primes:
    for n in range( prime,target+1):
        ways[n]+=ways[n - prime]

for ind, val in enumerate(ways):
    if val>5000:
        break
print(ind)
    

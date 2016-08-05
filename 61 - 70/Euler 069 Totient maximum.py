"""
Euler's Totient function, φ(n) [sometimes called the phi function], is used to determine the number of numbers less than n which are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine, φ(9)=6.

n	Relatively Prime	φ(n)	n/φ(n)
2	1	1	2
3	1,2	2	1.5
4	1,3	2	2
5	1,2,3,4	4	1.25
6	1,5	2	3
7	1,2,3,4,5,6	6	1.1666...
8	1,3,5,7	4	2
9	1,2,4,5,7,8	6	1.5
10	1,3,7,9	4	2.5
It can be seen that n=6 produces a maximum n/φ(n) for n ≤ 10.

Find the value of n ≤ 1,000,000 for which n/φ(n) is a maximum.
"""

#Equivalently we will try to minimize Totient(n)/n rather than maximize n/Totient(n)
#We will let F(x) = Totient(x)/x

# F(x) has the following properties:
# A) F(x) = F(x * (prime_in_x) )
# B) F(x) > F(x * (prime_not_in_x) )

#Thus to minimize F(x) for x below some limit:
# each prime factor of x should only be raised to the first power.
# multiplying x by a prime that isn't its factor (with a product < limit) will give a better answer 

#Thus the best answer is the product of the smallest primes such that the product < limit
#2*3*5*7*9*11*13*17 = 510510 which is <= 1 million
print(510510)

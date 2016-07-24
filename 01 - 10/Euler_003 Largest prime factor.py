"""
https://projecteuler.net/problem=3

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""
import time
start=time.clock()


#given the number 600851475143
number=600851475143

#divide by 2 until odd or 2 (if n was originally 2 ** k )
while( number % 2 == 0 and number > 2 ):
    number%=2

#divide number by its prime factors one by one
#until only its largest prime factor remains
#rather than spending time seperating the prime numbers from the odd ones
#we will just try to divide by all odd numbers
odd=3
while odd <= number ** 0.5:
    if number % odd == 0:
        number //= odd
    else:
        odd += 2

print("Answer",number,"computed in",(time.clock()-start)*1000,"ms")

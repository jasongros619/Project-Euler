"""
https://projecteuler.net/problem=16

215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""

import time
start = time.clock()

number = 2**1000
answer = 0
while number > 0:
    answer += number % 10
    number //= 10

print("Answer",answer,"computed in",(time.clock() - start) * 1000,"ms")

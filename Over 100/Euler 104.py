"""
The Fibonacci sequence is defined by the recurrence relation:

F_n = F_n−1 + F_n−2, where F_1 = 1 and F_2 = 1.
It turns out that F541, which contains 113 digits, is the first Fibonacci number for which the last nine digits are 1-9 pandigital (contain all the digits 1 to 9, but not necessarily in order). And F2749, which contains 575 digits, is the first Fibonacci number for which the first nine digits are 1-9 pandigital.

Given that Fk is the first Fibonacci number for which the first nine digits AND the last nine digits are 1-9 pandigital, find k.
"""
import time
start = time.clock()
from math import log

#returns the first 9 digits of the nth Fibonacci number
def fib_front(n):
    phi = (1 + 5**0.5)/2 #golden ratio
    log_Fib = n * log(phi,10) - log(5**0.5,10)
    return int( 10**(log_Fib%1 + 8) )

#returns if number is 1-9 pandigital
def pan(num):
    ans = 0
    while num > 0:
        ans += 10**(num%10)
        num //= 10
    return ans == 1111111110

#iterate through each Fibonaci number
fib_old = 1 #previous prime
fib_now = 1 #current prime
index   = 2 #index of current prime

while True:
    fib_next = (fib_old + fib_now) % 10**9
    fib_old = fib_now
    fib_now = fib_next
    index += 1

    if pan(fib_now):
        if pan( fib_front(index) ):
            break

print(index,time.clock()-start)

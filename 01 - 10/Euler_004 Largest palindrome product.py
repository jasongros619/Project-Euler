"""
https://projecteuler.net/problem=4

A palindromic number reads the same both ways. The largest palindrome
made from the product of two 2-digit numbers is 9009 = 91 × 99. Find
the largest palindrome made from the product of two 3-digit numbers.

"""
import time
start=time.clock()

def ispal(n):
    return str(n) == str(n)[::-1]




#loop through all 3 digit numbers with i<=j
#record largest product
largest = 0
for num1 in range(100,1001):
    for num2 in range(num1,1001):
        product = num1 * num2
        if ispal(product) and product > largest:
            largest = product
print("Answer is",largest,"copmuted in",(time.clock()-start)*1000,"ms")


"""
Powerful digit counts
Problem 63
The 5-digit number, 16807=75^5, is also a fifth power.
Similarly, the 9-digit number, 134217728=89^9, is a ninth power.

How many n-digit positive integers exist which are also an nth power?
"""
import math
import time
start = time.clock()

def digits(a,b):
    # a ^ b
    a = math.log(a,10)
    return math.floor(a*b) + 1

count=0
for a in range(1,1000):
    for b in range(1,1000):
        if b==digits(a,b):
            count+=1
        if digits(a,b)>b:
            break

print(count,time.clock()-start)

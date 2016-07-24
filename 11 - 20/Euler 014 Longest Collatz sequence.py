"""
https://projecteuler.net/problem=14

The following iterative sequence is defined for the set of positive integers:
n → n/2    (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million
"""

import time
start=time.clock()

collatzDic={}
#collatz[n] is number of iterations to 1
collatzDic[1]=0

longest=0
number=1

def fillDic(number,steps=0):
    #parent is the next collaltz number
    parent = number * 3 + 1 if number % 2 == 1 else number // 2

    #recursively make sure that the parent has the number of steps defined
    if collatzDic.get(parent,None)==None:
        fillDic(parent)

    #update the number of steps of the number
    collatzDic[number] = collatzDic[parent] + 1

longest = 0
best    = 1

for number in range(2,10**6):
    if collatzDic.get(number,None) == None:
        fillDic(number)
        if collatzDic[number] > longest:
            best    = number
            longest = collatzDic[number]


print("Answer",number,"computed in",(time.clock()-start)*1000,"ms")

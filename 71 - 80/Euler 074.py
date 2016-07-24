"""
Project Euler 74

You can form a sequence of numbers where the next number is the
sum of the factorial of digits of the previous number in the sequence.
As in  6 -> 120 ->(1! + 2! + 0!) 4 -> 24 ->(2! + 4!) 26 -> ...
and every sequence eventually converges into a loop.
The longest sequences have 60 numbers without repeating any.
How many sequences have 60 numbers?
"""
import time
start=time.clock()


factorial=[1,1,2,6,24,120,720,5040,40320,362880,3628800]

#calculates the sum of the factorial of the digits of 'n'
def factsum(n):
    if n < 10:
        return factorial[n]
    else:
        return factorial[n%10] + factsum(n//10)

#number of iterations before a repeat
steps={}

#the following numbers are given as the only loops that exist
steps[1]=1
steps[2]=1
steps[145]=1
steps[40585]=1

steps[871]=2
steps[45361]=2

steps[872]=2
steps[45362]=2

steps[169]=3
steps[363601]=3
steps[1454]=3

#determine number of steps for 'n'
def solvestep(n):
    #when n is not solved already
    if steps.get(n,None)==None:
        parent = factsum(n)
        solvestep(parent)
        steps[n]=steps[parent]+1

count=0
for i in range(10**6):
    solvestep(i)
    if steps[i]==60:
        count+=1

print(count)
print(time.clock()-start)

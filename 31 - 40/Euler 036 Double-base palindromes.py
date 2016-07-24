"""
Summery: What is the sum of all numbers < 1
million that are palindromic in base 10 and 2?
"""
import time
start = time.clock()
def ispal(n):
    ncopy=str(n)[::-1]
    return str(n)==ncopy

ans = 0
for i in range(1,10**6):
    #check if palindrome in base 10
    if ispal(i):
        #check if palindrome in base 2
        if ispal( bin(i)[2:]):
            ans += i

print(ans,time.clock()-start)

"""
A number chain is created by continuously adding the square of the digits in a number to form a new number until it has been seen before.

For example,

44 → 32 → 13 → 10 → 1 → 1
85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop. What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.

How many starting numbers below ten million will arrive at 89?
"""
import time
start = time.clock()

def next(n):
    return 0 if n == 0 else (n%10)**2 + next(n//10)

chain = [None]*(10**6)
chain[0] = False
chain[1] = False
chain[89] = True

def solve(n):
    if chain[n] == None:
        parent = next(n)
        if chain[n] == None:
            solve(parent)
        chain[n] = chain[parent]
    return chain[n]

print(sum([ 1 for i in range(1,10**6) if solve(i)]),time.clock())

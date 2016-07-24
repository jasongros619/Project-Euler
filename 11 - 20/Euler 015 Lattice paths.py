"""
https://projecteuler.net/problem=15

Starting in the top left corner of a 2×2 grid, and only being able to
move to the right and down, there are exactly 6 routes to the bottom
right corner.

(Six diagrams shown)

How many such routes are there through a 20×20 grid?
"""

#The point (x,y) has (x+y)! // (x! * y!) ways of getting to it.

import time
start=time.clock()

def fact(n):
    return 1 if n==0 else n * fact(n - 1)

ans=fact(40)//fact(20)**2

print("Answer",ans,"computed in",(time.clock()-start)*1000,"ms")

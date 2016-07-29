"""
Nim is a game played with heaps of stones, where two players take it in turn to remove any number of stones from any heap until no stones remain.

We'll consider the three-heap normal-play version of Nim, which works as follows:
- At the start of the game there are three heaps of stones.
- On his turn the player removes any positive number of stones from any single heap.
- The first player unable to move (because no stones remain) loses.

If (n1,n2,n3) indicates a Nim position consisting of heaps of size n1, n2 and n3 then there is a simple function X(n1,n2,n3) — that you may look up or attempt to deduce for yourself — that returns:

zero if, with perfect strategy, the player about to move will eventually lose; or
non-zero if, with perfect strategy, the player about to move will eventually win.
For example X(1,2,3) = 0 because, no matter what the current player does, his opponent can respond with a move that leaves two heaps of equal size, at which point every move by the current player can be mirrored by his opponent until no stones remain; so the current player loses. To illustrate:
- current player moves to (1,2,1)
- opponent moves to (1,0,1)
- current player moves to (0,0,1)
- opponent moves to (0,0,0), and so wins.

For how many positive integers n ≤ 2^30 does X(n,2n,3n) = 0 ?
"""

def isLoss(n):
    #the formula for NIM is:
    #a (XOR) b (XOR) c, with bitwise XOR
    #for values of n, 2n, and 3n
    return n ^ (2*n) ^ (3*n) == 0


#The following shows a pattern
for power in range(13):
    losses = len( [i for i in range(1,1 + 2**power) if isLoss(i)] )
    print("1 <= x <= 2^"+str(power)+" has "+str(losses) + " numbers")
"""
Prints:
1 <= x <= 2^0 has 1 numbers
1 <= x <= 2^1 has 2 numbers
1 <= x <= 2^2 has 3 numbers
1 <= x <= 2^3 has 5 numbers
1 <= x <= 2^4 has 8 numbers
1 <= x <= 2^5 has 13 numbers
1 <= x <= 2^6 has 21 numbers
1 <= x <= 2^7 has 34 numbers
1 <= x <= 2^8 has 55 numbers
1 <= x <= 2^9 has 89 numbers
Which are each the (power + 2)'th FIBONACCI numbers
"""

#return's nth Fibonacci number
def Fibonacci(n):
    phi = 5**0.5/2 + 1/2 #golden ratio
    return round((phi**n-(-phi)**(-n))/5**0.5)


print("Final answer:",Fibonacci(30))

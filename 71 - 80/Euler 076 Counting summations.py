"""
Summary: How many ways can you sum 100 with 2 or more positive numbers?
"""


"""
==========================================================
MATH to recursion relation
==========================================================
These are all the partitions of 7 with subsets of size <= 3
000 / 000 / 0
000 / 00 / 00
000 / 00 / 0 / 0
000 / 00 / 00
--------
00 / 00 / 00 / 0
00 / 00 / 0 / 0 / 0
00 / 0 / 0 / 0 / 0 / 0
0 / 0 / 0 / 0 / 0 / 0 / 0
They can be divided into two categories (as indicated by the line),
A) Those that are partitions of 4 with subsets of size < 4, with a subset of 3 added
B) Those that are partitions of 7 with subsets of size < 3.

Thus if W(n,m) is the number of partitions of 'n' with subsets of size <= 'm'
W(n,m+1) = W(n-m,m+1) + W(n, m)
For a base case W(0,0) = 1 and otherwise W(n,0) = 0
"""

LIMIT = 100
num_ways = [1] + [0] * LIMIT
#num_ways[i] = W(i,0)

for m in range(1,LIMIT):
    #if i >= m, then num_ways[i] is currently W(i,m)
    #and for i < m,  num_ways[i] is currently W(i,m+1)
    
    for n in range(m,LIMIT+1):
        #W(n,m+1)   = W(n,m)      + W(n-m, m+1)
        num_ways[n] = num_ways[n] + num_ways[n-m]

print(num_ways[LIMIT])

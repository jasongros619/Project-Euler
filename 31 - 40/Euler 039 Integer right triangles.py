"""
If p is the perimeter of a right angle triangle
with integral length sides, {a,b,c}, there are exactly
three solutions for p = 120, {20,48,52}, {24,45,51}, {30,40,50}.

For which value of p ≤ 1000, is the number of solutions maximised?
"""
import math

side1_start = int(1000 //(math.sqrt(2) + 2))

def issqr(x):
    return int(x**0.5)**2 == x

freq = {}
for side1 in range(side1_start,500):
    for side2 in range(1, side1 + 1):
        side3_sqr = side1**2 + side2**2
        perim = side1 + side2 + int(math.sqrt(side3_sqr))

        if perim > 1000:
            break
        if issqr( side3_sqr ):
            freq[perim] = freq.get(perim,0)+1

max_per = 0
max_num = 0
for perim in freq:
    if freq[perim] > max_num:
        max_num = freq[perim]
        max_per = perim
print( max_per)

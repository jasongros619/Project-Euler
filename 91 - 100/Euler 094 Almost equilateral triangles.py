"""
It is easily proved that no equilateral triangle exists with integral length
sides and integral area. However, the almost equilateral triangle 5-5-6 has
an area of 12 square units.

We shall define an almost equilateral triangle to be a triangle for which
two sides are equal and the third differs by no more than one unit.

Find the sum of the perimeters of all almost equilateral triangles with
integral side lengths and area and whose perimeters do not exceed one billion
(1,000,000,000).
"""

#Each triangle has side lengths, (s,s,s+1) or (s,s,s-1)

"""
We can create a list of small s which work.
By examining it, the following recurance relation forms
    s_0 = 1
    s_1 = 1
    s_n = 4*s_(n-1) + s_(n-2) + 2* (-1) ^ n
Additionally it alternates between (s,s,s+1) and (s,s,s-1)
The first two triangles (1,1,2) and (1,1,0) should not be added to final answer
These two triangles have 0 area.


At this point you can generate all perimeters below N in log(N) time.
I believe this is what the problem writers intended.
You can further examine it with math to solve in constant time.


We can solve explicitly for s_n using the recurrence relation.
Then we can solve explicitly for the n'th perimeter, P_n.
"""
Q = 2 + 3**0.5 #relevant constant ~ 3.7

def Perimeter(n):
    return Q ** (n) + Q ** (-n) + 2 * (-1) ** n
"""
To sum P_0 + P_1 + ... + P_N is actually quite easy.
It is the sum of 3 geometric series.
"""

#Sum of P_0 + P_1 + ... + P_n
def Perimeter_Sum(n):
    sum1 = (Q ** ( n+1) - 1) / (Q - 1)
    sum2 = (Q ** (-n-1) - 1) / (1/Q - 1)
    sum3 = 1 + (-1) ** n
    return round(sum1 + sum2 + sum3)
"""
Thus if you know the max 'n' which is easy to approximate,
you can find the sum in Constant time
"""



import math


def Main(LIMIT):
    #Solutions for very small values
    if LIMIT < 16:
        return 0
    if LIMIT < 50:
        return 16

    #Since every term of P_n goes to 0 except for Q^n,
    #the n for the biggest P_n below LIMIT is approximately:
    n = int(math.log(LIMIT,Q))

    #n may be off by 1 when close to a whole number
    if Perimeter(n) > LIMIT:
        n -= 1
    elif Perimeter(n+1) < LIMIT:
        n += 1

    return Perimeter_Sum(n) - 6
    #subtract 6 to remove triangles (2,1,1) and (0,1,1) with areas 0

    
print(Main(10**9))

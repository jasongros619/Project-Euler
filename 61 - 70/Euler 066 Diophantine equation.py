"""
Diophantine equation
Problem 66

Summary:
Consider an equation of the form x^2 – D*y^2 = 1
For every non-square D, there is a minimal solution x,y
where the equation holds and x,y > 0.


Find the value of D ≤ 1000 in minimal solutions of x for
which the largest value of x is obtained.
"""


import time
start=time.clock()

"""
See Chakravala method https://en.wikipedia.org/wiki/Chakravala_method
Function returns (x,y) such that x^2 - N*y^2 = 1
"""
def chakravala(N):
    #Return the minimal solution (x, y) for the Diophantine
    m = m0 = int(round(N**0.5))
    a = m
    b = 1
    k = m*m - N

    #no solution when N is square
    #returns 1,0
    if k == 0:
        return (1,0)
 
    while k != 1:
        # End if k in [-1, ±2], or k is ±4 and a or b is even
        if k == -1 or abs(k) == 2 or (abs(k) == 4 and not (a&1 and b&1)):
            # compose (a, b, k) with (a, b, k) and return solution
            return ((a*a + N*b*b)//abs(k), 2*a*b//abs(k))
 
        # find m such that: (a + b*m) % k == 0, abs(m^2 - N) is minimized
        diff = (m + m0) % abs(k)
        m_lo = m0 - diff
        m_hi = m_lo + abs(k)
        low = m_lo**2 - N
        high= m_hi**2 - N
        m = m_hi if low > high else m_lo
 
        #determine next iteration with (a, b, k) and (m, 1, m^2 - N)
        a_next = (m*a+N*b)//abs(k)
        b_next = (m*b+a)//abs(k)
        k_next = (m*m-N)//k
        a = a_next
        b = b_next
        k = k_next
        
    return (a, b)

max_x=0
max_i=0

for i in range(1,1001):
    X = chakravala(i)[0]
    if X > max_x:
        max_x = X
        max_i = i

print(max_i,time.clock()-start)

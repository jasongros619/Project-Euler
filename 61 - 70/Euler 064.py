import math
import time
start = time.clock()

#returns length of repeating digits of a continued fraction
def contlen(n):
    root = int(math.sqrt(n))

    #ignore square 'n'
    if root * root == n:
        return 0


    arr=[ (0,1,root) ]

    index = 0
    while True:
        t=arr[-1]
        m=t[0]
        d=t[1]
        a=t[2]
        
        m_next = a * d - m
        d_next = (n - m_next*m_next) // d
        a_next = (root + m_next) // d_next

        t=(m_next,d_next,a_next)
        if t in arr:
            return index-arr.index(t)+1
        else:
            arr.append(t)
            index +=1

ans = 0
for i in range(10001):
    if contlen(i)%2==1:
        ans += 1

print(ans, time.clock()-start)

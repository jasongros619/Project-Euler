"""

Summary:
See this for information about continued fractions <>
Using the continued fraction approximation for e,
what is the sum of the digits of the numerator of the
100th convergent of the continued fraction.

"""
import time
start = time.clock()

#calculate the numbers for the continued fraction
conv = [2,1,2,1,1]
for i in range(4,200,2):
    conv += [i,1,1]

#use math to find the 100th convergent's numerator

h=[2,3]
for i in range(2,101):
    h.append( conv[i]*h[i-1]+h[i-2] )

k = h[99]
ans = 0
while  k>0:
    ans += k%10
    k /= 10
    
print(ans,time.clock()-start)

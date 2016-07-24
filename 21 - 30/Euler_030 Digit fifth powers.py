"""
Project Euler #30
https://projecteuler.net/problem=30

Find the sum of all the numbers that can be written as the sum of fifth
powers of their digits
"""

import time
start=time.clock()

fifthsum=[]
for num in range(10):
    fifthsum[num] = num**5

#We can split a number such as 123456 into 12345 and 6 which are already solved
#It is easily provable nothing above 10^6 has this property
ans=0
for num in range(10,10**6):
    tail = num%10
    body= num//10
    fifthsum[num] = fifthsum[body] + tail ** 5
    if fifthsum[num] == num:
        ans += num


print("Answer",ans,"computed in",(time.clock()-start)*1000,"ms")

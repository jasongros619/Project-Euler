import time
start=time.clock()

import math

nums={}
for a in range(2,101):
    for b in range(2,101):
        #find log( a^b ) rounded at the 10th decimal place
        #check if you have already calculated this number before
        log_base = int( math.log( a ) * b * 10**10 )
        #check in constant time
        if nums.get(log_base,None)==None:
            nums[log_base]=True

print("Answer",len(nums),"computed in",(time.clock()-start)*1000,"ms")


import time
import math
start_time=time.clock()


#returns Greatest common factor of two numbers
def GCF(a,b):
    return a if b==0 else GCF(b,a%b)

count = 0
for den in range(4,12000):
    start = math.ceil(den/3)
    end = math.ceil(den/2)
    for num in range(start,end):
        if num%2!=0 or 0!=den%2:
            if GCF(num,den) == 1:
                count +=1

print(count)
print(time.clock()-start_time)
        

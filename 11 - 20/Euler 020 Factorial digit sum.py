import time
start=time.clock()

def factorial(n):
    return 1 if n == 0 else n* factorial(n-1)

fact = factorial(100)
mysum = 0
while fact > 10:
    mysum += fact % 10
    fact //= 10

print("Answer",mysum,"computed in",(time.clock() - start) * 1000,"ms")

#ans=648

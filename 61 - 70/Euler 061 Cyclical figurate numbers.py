import time
times=time.time()

"""
Cyclical figurate numbers
Problem 61

Summary:
Find the only ordered set of six 4 digit numbers for which there
are a triangular, square, pentagonal, hexagonal, heptagonal, and
octagonal number represented by a different number in the set.

Additionally, the first 2 digits of every number must match the
last 2 digits of the preceding number.

"""
import time
start_time = time.clock()


#Returns list of 4 digit numbers that are n-gon numbers
def polynumbers(n):
    #returns x'th n-gon number
    def calc(n,x):
        a_coef = [ 1, 1, 3, 2, 5, 3]
        b_coef = [ 1, 0,-1,-1,-3,-2]
        c_coef = [ 2, 1, 2, 1, 2, 1]
        a = a_coef[n-3]
        b = b_coef[n-3]
        c = c_coef[n-3]
        return (x*(a*x + b)) // c
    
    arr = [ calc(n,i) for i in range(1,150) ]
    return [ i for i in arr if i >= 1000 and i<10000]

#list of list of polygon numbers
nums = [ polynumbers(i) for i in range(3,9) ]

#Return what shape a number is
def polytype(n):
    for i in range(8,2,-1):
        if n in nums[i-3]:
            return i

#start[XY] is a list of numbers starting with "XY"
start = [ [] for i in range(100) ]
for shape in nums:
    for num in shape:
        front = num//100
        start[front].append(num)

#Returns list of numbers starting with the same
#2 digits as this number's last 2 digits
def possible(n):
    end = n%100
    return start[end]


ans = None
for octs in nums[-1]:
    for p1 in possible(octs):
        for p2 in possible(p1):
            for p3 in possible(p2):
                for p4 in possible(p3):
                    for p5 in possible(p4):
                        if octs in possible(p5):
                            #make a 6 part chain
                            chain = [p1, p2, p3, p4, p5, octs]
                            #check if it has one of each type
                            types = [ polytype(num) for num in chain ]
                            if sorted(types) == [3,4,5,6,7,8]:
                                ans = chain

print(sum(ans),time.clock()-start_time)

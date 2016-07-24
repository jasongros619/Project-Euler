"""
Cubic permutations
Problem 62

Summary: Find the smallest cube for which exactly
five permutations of its digits are cube.
"""
import time
start = time.clock()

#value unique to digits, but not order
def myhash(n):
    ans = 0
    while n>0:
        ans += 100**(n % 10)
        n //= 10
    return ans

n = 0
digits = 1
ans = None

while ans==None:
    #hash all the cubes into the dictionary
    dic = {}
    while n**3 < 10**digits:
        
        cube = n**3
        key = myhash(cube)
        dic[key]=dic.get(key,[]) + [cube]

        n += 1
    #check for hash values with enough permutations 
    for key in dic:
        if len(dic[key])==5:
            if ans == None:
                ans = min(dic[key])
            else:
                ans = min(ans,min(dic[key]))

    digits +=1

print(ans,time.clock()-start)


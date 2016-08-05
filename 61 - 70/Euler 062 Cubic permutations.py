"""
Cubic permutations
Problem 62

Summary: Find the smallest cube for which exactly
five permutations of its digits are cube.
"""
import time
start = time.clock()

#anagrams will have collisions
def myhash(n):
    primes = [ 2, 3, 5, 7,11,13,17,19,23,29]
    ans = 1
    while n>0:
        ans *= primes[n % 10]
        n //= 10
    return ans

cubes = {} #hashtable for each cubes
n = 0      #starting number (to be cubed)
ans = None #final answer

while ans==None:
    cube = n**3
    key = myhash(cube)
    cubes[key] = cubes.get(key,[]) + [cube]
    if len(cubes[key]) == 5:
        ans = min(cubes[key])
    else:
        n += 1

print(ans,time.clock()-start)


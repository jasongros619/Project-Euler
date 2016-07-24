target = 100
primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,91,97]
ways=[0]*(target+1)

ways[0]=1

for i in range(len(primes)):
    for j in range( primes[i],target+1):
        ways[j]+=ways[j - primes[i]]

for w in ways:
    if w>5000:
        print(ways.index(w))
        break
    

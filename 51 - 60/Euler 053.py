"""
How many numbers made by (n choose c) have values over 1 million
for n <= 100 ?
"""
import math

log_fact=[0,0]
for i in range(2,101):
    log_fact.append( math.log(i,10)+log_fact[i-1])

def isbig(n,c):
    return log_fact[n] - log_fact[n-c] - log_fact[c]

count = 0
for n in range(1,101):
    for c in range(1,n):
        val = isbig(n,c)
        if val > 6:
            count +=1
print(count)

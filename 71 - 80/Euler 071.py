goal=(3,7)
best=(2,5)

def better(n,d):
    #d1=g-best
    #d2=g-f2
    #d2<d1 <=> g-f2<g-best <=> f2>best
    #f=(n,d)
    #2/4 1/2
    return ( n*best[1]>d*best[0] )

for den in range(8,10**6+1):
    num=int(3*den/7)
    if better(num,den):
        if num*7 != den*3:
            best=(num,den)

print(best)

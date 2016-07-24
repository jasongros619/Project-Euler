def inrect(a,b,x,y):
    return (1+x-a)*(1+y-b)


def rects(x,y):
    out=0
    for a in range(1,x+1):
        for b in range(1,y+1):
            out+=inrect(a,b,x,y)
    return out


area=(1,1,1)
for x in range(1,101):
    for y in range(1,101):
        k=(x,y,rects(x,y))
        if k[2]>area[2] and k[2]<2*10**6:
            area=k
print(area[0]*area[1])

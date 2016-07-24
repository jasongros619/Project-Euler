"""
Right triangles with integer coordinates
Problem 91

The points P (x1, y1) and Q (x2, y2) are plotted at integer
co-ordinates and are joined to the origin, O(0,0), to form triangle OPQ.

Given that 0 <= x1, y1, x2, y2 <= 50, how many right triangles can be formed?
"""

#There are 4 places a right angle can be:
#a) Origin - has size^2 triangles - triangle (x,0),(0,y),(0,0) for x,y>0
#b) x-axis - has size^2 triangles - triangle (x,0),(x,y),(0,0) for x,y>0
#c) y-axis - has size^2 triangles - triangle (x,y),(0,y),(0,0) for x,y>0
#d) elseware: ? triangles

size = 50
count = 3 * size ** 2 #for a), b), c)

def GCF(a,b): #greatest common factor
    return a if b==0 else GCF(b,a%b)

#Triangles with point @, with coordinates (x,y), as it's right angle
#will have another corner in either region
# R1 or R2 of size (x, Size - y) and (Size - x, y) respectively
# |    |
# | R1 |
# |____|____
# |    @
# |   /| R2
# |  / |
# | /  |
# |/   |
# *=========
for Y in range(1,size+1):
    for X in range(1,size+1):
        gcf = GCF(X,Y)
        x_small = X // gcf 
        y_small = Y // gcf 
        r1 = min( (size-Y) // x_small, X // y_small)
        r2 = min( (size-X) // y_small, Y // x_small)
        count += r1 + r2

print(count)

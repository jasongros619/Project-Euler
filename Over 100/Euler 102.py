"""
Three distinct points are plotted at random on a Cartesian plane, for which -1000 ≤ x, y ≤ 1000, such that a triangle is formed.

Consider the following two triangles:

A(-340,495), B(-153,-910), C(835,-947)

X(-175,41), Y(-421,-714), Z(574,-645)

It can be verified that triangle ABC contains the origin, whereas triangle XYZ does not.

Using triangles.txt (right click and 'Save Link/Target As...'), a 27K text file containing the co-ordinates of one thousand "random" triangles, find the number of triangles for which the interior contains the origin.

NOTE: The first two examples in the file represent the triangles in the example given above.
"""
import time
start=time.clock()

class Vect(object):
    def __init__(self,x,y):
        self.x=x
        self.y=y        
    def __sub__(self,other):
        x = self.x - other.x
        y = self.y - other.y
        return Vect(x,y)
    def __mul__(self,other):
        x = self.x * other
        y = self.y * other
        return Vect(x,y)
    def dot(self,other):
        return self.x * other.x + self.y * other.y

#returns of triangle defined by vectors P1,P2,P3 contains the origin    
def inOrigin(P1,P2,P3):
    #Calculate vectors
    v0 = P3 - P1
    v1 = P2 - P1
    v2 = Vect(0,0) - P1

    #Calculate dot products
    dot00 = v0.dot(v0)
    dot01 = v0.dot(v1)
    dot02 = v0.dot(v2)
    dot11 = v1.dot(v1)
    dot12 = v1.dot(v2)

    #Compute values
    Den = (dot00 * dot11 - dot01 * dot01)
    u = (dot11 * dot02 - dot01*dot12)
    v = (dot00 * dot12 - dot01*dot02)

    return (u>=0) and (v>=0) and (u + v < Den)


count = 0
file  = open("p102_triangles.txt","r")
for line in file:
    #points = [x0,y0,x1,y1,x2,y2]
    points = [int(i) for i in line.split(",")]

    #Create vectors for corners of triangle
    P0 = Vect(points[0],points[1])
    P1 = Vect(points[2],points[3])
    P2 = Vect(points[4],points[5])

    if inOrigin(P0,P1,P2):
        count += 1

file.close()
print(count,time.clock()-start)

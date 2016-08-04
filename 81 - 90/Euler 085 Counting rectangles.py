"""
By counting carefully it can be seen that a rectangular grid measuring 3 by 2
contains eighteen rectangles:

(18 Examples shown)
> 6 1x1 rectangles
> 4 2x1 rectangles
> 2 3x1 rectangles
> 3 1x2 rectangles
> 2 2x2 rectangles
> 1 3x2 rectangles

Although there exists no rectangular grid that contains exactly two million
rectangles, find the area of the grid with the nearest solution.
"""

#Using math, there are x*(x+1)*y*(y+1) rectangles that can be placed in an x by y
#rectangle. Function returns the difference between the number of rectangles that
#can be placed in an x by y rectangle and 2 million (the target number)
def error(x,y):
    return ( ( x*(x+1)*y*(y+1) )//4 - 2000000)

#Now to loop over values of x and y to find the smallest error
TARGET = 2000000        #Target number of rectangles
x = 1                   #smallest possible value of x. Will be increased
y =  int(TARGET**0.5)   #largest possible value of y. Will be decreased
diff = error(x,y)       #difference between number of rectangles and 2 million
best = abs(diff)        #smallest error
area = x * y            #smallest difference's area

while y >= x:
    y = y-1 if diff > 0 else y
    x = x+1 if diff < 0 else x
    diff = error(x,y)
    if abs(diff) < best:
        best = abs(diff)
        area = x*y
print(area)

"""
https://projecteuler.net/problem=18

By starting at the top of the triangle below and moving to adjacent
numbers on the row below, the maximum total from top to bottom is 23.

   3
  7 4
 2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

(Triangle of size 15 shown. Pyramid of numbers is saved as "Problem 18 Pyramid.txt")
"""


import time
start=time.clock()

rows=15

#create a 2d array of the pyramid's numbers
file = open("Problem 18 Pyramid.txt")
pyramid = []
for line in file:
    split = line.split(" ")
    pyramid.append( [int(i) for i in split ] )



#recursively move up each layer
#adding to each element, the max of the two below it
#    9          9         9    ->    26    => 26
#   7 8        7 8  ->  14 17      15  17
#  4 5 6  ->  5 7 9    5  7  9    5   7  9
# 0 1 2 3    0 1 2 3  0  1  2 3  0  1   2 3
for row in range(14)[::-1]:
    for col in range(row+1):
        highest = max( pyramid[row + 1][col], pyramid[row + 1][col + 1])
        pyramid[row][col] += highest
    
print("Answer",pyramid[0][0],"computed in",(time.clock()-start)*1000,"ms")

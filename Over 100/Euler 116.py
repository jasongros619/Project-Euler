"""
A row of five black square tiles is to have a number of its tiles replaced with coloured oblong tiles chosen from red (length two), green (length three), or blue (length four).

If red tiles are chosen there are exactly seven ways this can be done.
If green tiles are chosen there are three ways.
And if blue tiles are chosen there are two ways.

	
	
Assuming that colours cannot be mixed there are 7 + 3 + 2 = 12 ways of replacing the black tiles in a row measuring five units in length.

How many different ways can the black tiles in a row measuring fifty units in length be replaced if colours cannot be mixed and at least one coloured tile must be used?

NOTE: This is related to Problem 117.
"""

LENGTH = 50


#How many ways can you make Nx1 with 1x1 and Mx1 tiles? (you can use 0 of either)
#Note that for each arrangement, you can remove the last tile and you will have
#Each arrangement of size (N-1) x 1 and each (N - M) x 1 arrangement.
#Thus Ways_N = Ways_(N-1) + Ways_(N-M)

#base cases for each color
red = [1,1]
gre = [1,1,1]
blu = [1,1,1,1]

for i in range(LENGTH):
    red.append(red[-1] + red[-2])
    gre.append(gre[-1] + gre[-3])
    blu.append(blu[-1] + blu[-4])

#dont count only 1x1 in final answer. arrangement appears once in each color
print( red[50]+blu[50]+gre[50] - 3)

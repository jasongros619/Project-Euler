"""
Using a combination of black square tiles and oblong tiles chosen from: red tiles measuring two units, green tiles measuring three units, and blue tiles measuring four units, it is possible to tile a row measuring five units in length in exactly fifteen different ways.
(Picture of all arrangements of size 1x5 composed of tiles of size 1x1,1x2,1x3 and 1x4 put together.)
(Order matters)
How many ways can a row measuring fifty units in length be tiled?

NOTE: This is related to Problem 116.
"""
#ways[i] = # of ways to create an 'i'-long thing
ways=[1,1,2,4] #base cases

#from every arrangement of size (N-1), you can add a 1x1 rect at end and create an Nx1 arrangement
#from every arrangement of size (N-2), you can add a 2x1 rect at end and create an Nx1 arrangement
#from every arrangement of size (N-3), you can add a 3x1 rect at end and create an Nx1 arrangement
#from every arrangement of size (N-4), you can add a 4x1 rect at end and create an Nx1 arrangement
#Each of these arrangements is distinct.
#Every arrangement of size N is from one of these, as you can remove the last tile.

#Thus W_n = W_(n-1) + W_(n-2) + W_(n-3) + W_(n-4)

for i in range(4,51):
    ways.append( sum(ways[-4:] ) )

print(ways[-1])


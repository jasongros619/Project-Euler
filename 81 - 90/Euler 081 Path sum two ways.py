"""
In the 5 by 5 matrix below, the minimal path sum from the top left to the
bottom right, by only moving to the right and down, is indicated in bold
red and is equal to 2427.

| 131  673  234  103   18 |
|  |                      |
| 201-> 96->342  965  150 |
|            |            |
| 630  803  746->422  111 |
|                 |       |
| 537  699  497  121  956 |
|                 |       |
| 805  732  524   37->331 |

Find the minimal path sum, in matrix.txt (right click and "Save Link/Target
As..."), a 31K text file containing a 80 by 80 matrix, from the top left to
the bottom right by only moving right and down.
"""
inf = float("infinity")
SIZE = 80

#Create a 2d grid from input file.
#Add a layer of Infinity values to the top and left of grid
file=open("p081_matrix.txt","r")
arr=[ [inf for i in range(SIZE+1)] ]
for line in file:
    arr.append( [inf] + [int(i) for i in line.split(",")] )
file.close()

#Shortest path to (x,y) is the sum of (x,y) and the
#minimum of the shortest path to (x-1, y) and (x, y-1).
for x in range(1,SIZE+1):
    for y in range(1,SIZE+1):
        if not (x,y) == (1,1):
            arr[y][x] += min(arr[y-1][x],arr[y][x-1])

print(arr[SIZE][SIZE])

"""
Comparing two numbers written in index form like 211 and 37 is not difficult,
as any calculator would confirm that 2^11 = 2048 < 3^7 = 2187.

However, confirming that 632382518061 > 519432525806 would be much more
difficult, as both numbers contain over three million digits.

Using base_exp.txt (right click and 'Save Link/Target As...'), a 22K text
file containing one thousand lines with a base/exponent pair on each line,
determine which line number has the greatest numerical value.

NOTE: The first two lines in the file represent the numbers in the example
given above.
"""

import time
start = time.clock()
import math

myfile=open("p099_base_exp.txt","r")
max_val = 0
max_ind = None

for i in range(1000):
    line=myfile.readline()[:-1].split(",")
    base=int(line[0])
    exponent=int(line[1])

    val = math.log(base) * exponent
    if val > max_val:
        max_val = val
        max_ind = i + 1
myfile.close()

print(max_ind,time.clock()-start)

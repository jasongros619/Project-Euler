"""
Summary:
40755 is the 285th Triangular number, 165th
pentagonal number and 143 Hexagonal number

Find the next triangular number that is also
pentagonal and hexagonal.
"""
import time
start = time.clock()

"""
from math, every hexagonal number is triangular,
so this problem simplifies to find the next
pentagonal and hexagonal number
we will compare pentagonal and hexagonal numbers,
incrementing the smaller until the two are even
"""

#functions for returning the n'th (polygon) number
hex_num = lambda x: x*x*2 - x
pen_num = lambda x: (x*x*3 - x)//2

#indices for keeping track of which numbers are being checked
hex_ind = 144 #given indice +1
pen_ind = 166 #given indice +1

#values of then (polygon)_ind 'th (polygon) number
hex_val = hex_num(hex_ind)
pen_val = pen_num(pen_ind)

#comparing increasily larger pentagonal and hexagonal
#numbers until the two are even
while hex_val != pen_val:
    if hex_val < pen_val:
        hex_ind += 1
        hex_val = hex_num( hex_ind)
    if hex_val > pen_val:
        pen_ind += 1
        pen_val = pen_num( pen_ind)

print(pen_val,time.clock()-start)

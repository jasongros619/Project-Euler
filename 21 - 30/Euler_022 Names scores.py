"""
https://projecteuler.net/problem=22

Using names.txt (right click and 'Save Link/Target As...'), a 46K text
file containing over five-thousand first names, begin by sorting it
into alphabetical order. Then working out the alphabetical value for
each name, multiply this value by its alphabetical position in the
list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN,
which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the
list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""

import time
start=time.clock()

myfile = open("p022_names.txt","r")
nameString = myfile.read()
nameList   = nameString.split(",")
nameList.sort()

def score(name):
    letters = '"ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    out = 0
    for letter in name:
        out += letters.index(letter)
    return out

total = 0
for i in range( len(nameList) ):
    name = nameList[i]
    total += (i + 1) * score( name )

print("Answer",total,"computed in",(time.clock()-start)*1000,"ms")

"""
By replacing each of the letters in the word CARE with 1, 2, 9, and 6
respectively, we form a square number: 1296 = 362. What is remarkable
is that, by using the same digital substitutions, the anagram, RACE,
also forms a square number: 9216 = 962. We shall call CARE (and RACE)
a square anagram word pair and specify further that leading zeroes are
not permitted, neither may a different letter have the same digital
value as another letter.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text
file containing nearly two-thousand common English words, find all the
square anagram word pairs (a palindromic word is NOT considered to be
an anagram of itself).

What is the largest square number formed by any member of such a pair?

NOTE: All anagrams formed must be contained in the given text file.
"""
import time
start = time.clock()

#returns a value for each swapping of digits/letters of 2 distinct strings
#given ABCD and BCAD, it would return '1203' and '2013'
def trans_hash(value1,value2):
    val1 = [str(value2.index(letter)) for letter in value1]
    val2 = [str(value1.index(letter)) for letter in value2]
    return [ "".join(val1), "".join(val2) ]


#creates a hashtable with anagrams put in the same slot
#delete all keys with no collisions
word_anagrams = {}
file = open("p098_words.txt","r")
for element in (file.readline()[1:-1]).split("\",\""):
    hashval = "".join(sorted(str(element)))
    word_anagrams[hashval] = word_anagrams.get(hashval,[]) + [element]
single = [key for key in word_anagrams if len(word_anagrams[key]) < 2]
for key in single:
    del word_anagrams[key]
file.close()


#for each pair of words within an anagram calculate its transformation
#then have 'transforms' store all transformation values we care about
transforms = []
for key in word_anagrams:
    words = word_anagrams[key]
    for ind1 in range(1,len(words)):
        for ind2 in range(ind1):
            word1 = words[ind1]
            word2 = words[ind2]
            transforms += trans_hash(word1,word2)


#Iterate over every square (in decreasing order)
#add it to the hashtable with its other anagrams
#check if it with any other of its anagrams are a desired transformation
#first sqr with property is largest and thus answer
ans = None
num_anagrams = {}
for i in range(31622,0,-1):
    sqr = i*i
    hashval = "".join(sorted(str(sqr)))
    num_anagrams[hashval] = num_anagrams.get(hashval,[]) + [sqr]

    trans = ["",""]
    for number in num_anagrams[hashval][:-1]:
        trans = trans_hash(str(number),str(sqr))
        if trans[0] in transforms or trans[1] in transforms:
            ans = sqr if sqr > number else number
            break
    if ans != None:
        break

print(ans,time.clock()-start)



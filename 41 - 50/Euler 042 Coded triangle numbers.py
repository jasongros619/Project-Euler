"""
The nth term of the sequence of triangle numbers is given
by, t_n = n(n+1)/2; so the first ten triangle numbers are:
1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding
to its alphabetical position and adding these values we form a
word value. For example, the word value for SKY is
19 + 11 + 25 = 55 = t_10. If the word value is a triangle number
then we shall call the word a triangle word.

How many words are triangle in words.txt
"""

#n is triangular, the expression is a whole number
def istri(n):
    p = (2*n + 1/4)**0.5 - 0.5
    return abs(p-round(p)) < 0.00001

def wordval(word):
    value = lambda x: " ABCDEFGHIJKLMNOPQRSTUVWXYZ".index(x)
    values = [value(letter) for letter in word]
    return sum(values)

count = 0
file = open("p042_words.txt")
a = file.split(",")
print(len(a))
for line in file:
    words = line.split(",")
    for word in words:
        if istri( wordval( word[1:-1] )):
            count += 1
print(count)
    





































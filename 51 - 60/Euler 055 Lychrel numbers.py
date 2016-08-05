"""
If we take 47, reverse and add, 47 + 74 = 121, which is palindromic.

Not all numbers produce palindromes so quickly. For example,

349 + 943 = 1292,
1292 + 2921 = 4213
4213 + 3124 = 7337

That is, 349 took three iterations to arrive at a palindrome.

Although no one has proved it yet, it is thought that some numbers,
like 196, never produce a palindrome. A number that never forms a
palindrome through the reverse and add process is called a Lychrel
number. Due to the theoretical nature of these numbers, and for the
purpose of this problem, we shall assume that a number is Lychrel
until proven otherwise. In addition you are given that for every
number below ten-thousand, it will either (i) become a palindrome
in less than fifty iterations, or, (ii) no one, with all the
computing power that exists, has managed so far to map it to a
palindrome.

How many Lychrel numbers are there below ten-thousand?
"""

import time
start=time.clock()
nums=[]

#reverses int faster than int( str(n)[::-1] ) ?
def backwards(n):
    ans = 0
    while n>0:
        ans *= 10
        ans += n%10
        n  //= 10
    return ans


def lych(n):
    for count in range(50):
        n = n + backwards(n)
        if str(n) == str(n)[::-1]:
            return True
    return False

count=0
for i in range(10**4):
    if not lych(i):
        count+=1

print(count)
print(time.clock()-start)

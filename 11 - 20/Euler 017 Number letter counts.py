"""
https://projecteuler.net/problem=17

If the numbers 1 to 5 are written out in words: one, two, three, four,
five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written
out in words, how many letters would be used?
"""

import time
start=time.clock()


ones=["","one","two","three","four","five","six","seven","eight",
      "nine","ten","eleven","twelve","thirteen","fourteen",
      "fifteen","sixteen","seventeen","eighteen","nineteen"]
tens=["","","twenty","thirty","forty","fifty","sixty",
      "seventy","eighty","ninety"]

#returns string for n < 100
def low(n):
    dig1 = n // 10
    dig2 = n % 10

    if n < 20:
        return ones[n]
    else:
        return tens[dig1] + ones[dig2]

#returns string for 0 <= n <= 1000
def name(n):
    #edge cases
    if n==0:
        return "zero"
    if n<100:
        return low(n)
    if n==1000:
        return "onethousand"

    #assume  100 <= n < 1000 which is 3 digits
    digit1 = n // 100
    digit23 = n % 100

    if digit23==0:
        return ones[digit1]+"hundred"
    else:
        return ones[digit1]+"hundred"+"and"+low(digit23)

ans=0
for i in range(1,1001):
    ans += len( name(i) )
print(ans,(time.clock()-start)*1000,"ms")


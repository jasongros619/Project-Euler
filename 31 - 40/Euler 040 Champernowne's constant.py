"""
An irrational decimal fraction is created by concatenating
the positive integers:
0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.
If d_n represents the nth digit of the fractional part.

Find the value of the following expression.
d_1 × d_10 × d_100 × d_1000 × d_10000 × d_100000 × d_1000000
"""
n=1         #number being iterated
digits = 1  #number of digits of n
length = 0  #length of concatinating 1 through n
goal = 1    #index of the special digits
ans = 1     #final answer

while goal <= 10**6:
    #check if it reaches the goal
    if length + digits >= goal:
        index = goal - length - 1
        ans *= int(str(n)[index])
        goal *= 10

    length += digits
    n += 1
    if n == 10**digits:
        digits += 1
        

print(ans)

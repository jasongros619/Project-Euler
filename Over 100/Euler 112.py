"""
Working from left-to-right if no digit is exceeded by the digit to its left it is called an increasing number; for example, 134468.

Similarly if no digit is exceeded by the digit to its right it is called a decreasing number; for example, 66420.

We shall call a positive integer that is neither increasing nor decreasing a "bouncy" number; for example, 155349.

Clearly there cannot be any bouncy numbers below one-hundred, but just over half of the numbers below one-thousand (525) are bouncy. In fact, the least number for which the proportion of bouncy numbers first reaches 50% is 538.

Surprisingly, bouncy numbers become more and more common and by the time we reach 21780 the proportion of bouncy numbers is equal to 90%.

Find the least number for which the proportion of bouncy numbers is exactly 99%.
"""
import time
start = time.clock()

def is_bouncy(n):
    up=False
    down=False
    
    prev_digit=n%10
    n //= 10
    while(n>0):
        next_digit=n%10
        if next_digit>prev_digit:
            up=True
        if next_digit<prev_digit:
            down=True
        if up and down:
            return True
        prev_digit=next_digit
        n //= 10
    return False


count=0 #number of bouncy numbers
i=0     #number of numbers tried
while( 99*i>count*100 or i==0):
    for j in range(100):
        i+=1
        if is_bouncy(i):
            count+=1

print(i,time.clock()-start)

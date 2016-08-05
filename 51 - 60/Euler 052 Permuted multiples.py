"""
It can be seen that the number, 125874, and its double, 251748,
contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x,
and 6x, contain the same digits.
"""
#collisions occur with anagrams
def digit_hash(n):
    return 0 if n==0 else 10**(n%10) + digit_hash(n//10)

#checks if 2x, 3x, ... 6x are anagrams of x
def main_test(n):
    hashed = digit_hash(n)
    for i in range(2,7):
        if digit_hash(n*i) != hashed:
            return False
    return True

#since n and 6n must have the same number of digits, we only need to check
# 1
# 10, 11, 12, ... , 16
# 100, 101, 102, ... , 166
# 1000, 1001, 1002, ... , 1666
# ...
# 10 ^ n , ... , 10 ^ (n+1) // 6

digits = 1
ans = None
while ans == None:
    num = 10**(digits-1)
    while num <= (10**digits)//6:
        if main_test(num):
            ans = num
            break
        num += 1
    digits += 1

print(ans)

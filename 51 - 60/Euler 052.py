"""

"""
#collisions occur with different
#orders of same digits
def digit_hash(n):
    return 0 if n==0 else 10**(n%10) + digit_hash(n//10)

def main_test(n):
    hashed = digit_hash(n)
    for i in range(2,7):
        if digit_hash(n*i) != hashed:
            return False
    return True

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

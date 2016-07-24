"""
Summary:
Take a number, say 192. If you multiply it by each
1, 2, 3 and concatenate the results, you get 192384576
which contains the digits 1 through 9 exactly once.

What is the largest result possible when concatenating
products of a number with (1,2,...n) where n > 1 ?
"""


"""
Note that when n = a number, some restrictions can be made
or else the products concatenated wont have 9 digits
n=2 5000 < X < 9999 (X*100002)
n=3 100  < X <  334 (X*1002003)
n=4 25   < X <   34 (X*10203004)
n=5 5    < X <    9 (X*102030405)
and when n=9, result = 123456789

Since a pandigital number is divisible by 9 and
none of the numbers multiplied by X above are divisible by
3 raised to the second power, X must be a multiple of 3.
"""

N    =[    2,  3, 4, 5]
small=[ 5001,102,27, 6] #smalles mult of 3 >= min
large=[10000,334,34,10] #smallest int > limit

def mult(num,n):
    ans = ""
    for i in range(1,n+1):
        ans += str(num*i)
    return ans

ans = 123456789
for i in range(4):
    n = N[i]
    for x in range(small[i],large[i],3):
        concat = mult(x,n)
        if "".join(sorted(concat)) == "123456789":
            if int(concat) > ans:
                ans = int(concat)
print(ans)

"""
The number, 1406357289, is a 0 to 9 pandigital number because
it is made up of each of the digits 0 to 9 in some order, but
it also has a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In
this way, we note the following:

d2d3d4 = 406 is divisible by 2
d3d4d5 = 063 is divisible by 3
d4d5d6 = 635 is divisible by 5
d5d6d7 = 357 is divisible by 7
d6d7d8 = 572 is divisible by 11
d7d8d9 = 728 is divisible by 13
d8d9d10 = 289 is divisible by 17
Find the sum of all 0 to 9 pandigital numbers with this property.
"""
import itertools

#digits[i] = (start_digit, end_digit, divisible)
digits = [
    (1,4,2),
    (2,5,3),
    (3,6,5),
    (4,7,7),
    (5,8,11),
    (6,9,13),
    (7,10,17)
]
def check(arr,start,end,divisible):
    num = 0
    for i in range(start,end+1):
        num *= 10
        num += int(arr[i])
    return num % divisible == 0

answers = {}
for end in itertools.permutations('012346789',4):
    arr = ["5"] + list(end)
    good = True
    if not check(arr,0,2,11):
        good = False
    if not check(arr,1,3,13):
        good = False
    if not check(arr,2,4,17):
        good = False

    if good:
        for start in itertools.permutations('012346789',5):
            arr2 = list(start) + arr

            if check(arr2,1,3,2) and check(arr2,2,4,3) and check(arr2,4,6,7):
                if ''.join(sorted(arr2)) == "0123456789":
                    answers[ int( ''.join(arr2) ) ]=True

ans = 0
for key in answers:
    ans += key
print(ans)

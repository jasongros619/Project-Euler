"""
The number 512 is interesting because it is equal to the sum of its digits raised to some power: 5 + 1 + 2 = 8, and 8^3 = 512. Another example of a number with this property is 614656 = 28^4.

We shall define an to be the nth term of this sequence and insist that a number must contain at least two digits to have a sum.

You are given that a_2 = 512 and a_10 = 614656.

Find a_30.
"""

#Lets make an assumption that a_30 has at most 100 digits
MAX_DIG_SUM = 9*50
MAX_VALUE = 10**50 - 1

def digitSum(n):
    return 0 if n==0 else n%10 + digitSum(n//10)

ans=[]
for digit_sum in range(2,MAX_DIG_SUM):
    #compute all powers of (digit_sum)
    #add each to 'ans' if it has correct Digit Sum
    current = digit_sum * digit_sum
    while current < MAX_VALUE:
        if digitSum(current) == digit_sum:
            ans.append(current)
        current *= digit_sum

            
ans = sorted(ans)
print(ans[29])
#answer ranked 30 of 96 calculated entries in the sequence

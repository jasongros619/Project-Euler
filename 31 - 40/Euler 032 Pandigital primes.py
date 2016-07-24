"""
Find the sum of all products such that num1 * num2 = product
where num1, num2, and product concatenated together contain the
digits 1 through 9.

Hint: Some products may be produced in multiple ways. Only count
the product once
"""

#if a,b,c concatenated contains digits 1-9
def ispan(a,b,c):
    
    #for n>0, returns sum 10 ^ (each digit)
    def myhash(n):
        return 0 if n==0 else 10**(n%10) + myhash(n//10)

    return myhash(a) + myhash(b) + myhash(c) == 1111111110


#The numbers together are 1-9 pandital only if:
#a 2 digit number x 3 digit number
#a 1 digit number x 4 digit number
products = {}

for digit1 in range(1,10):
    for digit4 in range(1000,10000):
        product = digit4 * digit1
        if product >= 10**5:
            break
        
        if ispan(digit1, digit4, product):
            products[product] = True

for digit2 in range(10,100):
    for digit3 in range(100,1000):
        product = digit3 * digit2
        if product >= 10**5:
            break

        if ispan(digit2, digit3, product):
            products[product] = True

print( sum(products.keys()) )

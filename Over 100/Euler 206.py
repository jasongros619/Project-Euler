"""
Find the unique positive integer whose square has the form 1_2_3_4_5_6_7_8_9_0,
where each “_” is a single digit.
"""
import time
start = time.clock()

#Return's the nth digit
def digit(n,pos):
    n //= 10**pos
    return n%10

#Returns if 'n' has matching digits of 1_2_3_4_5_6_7_8_9_0
def isAns(n):
    digits = [] #every other digit (ones, hundreds, ten thousands, ...)
    while n != 0:
        digits.append(n % 10)
        n //= 100
    return digits == [0,9,8,7,6,5,4,3,2,1]

#To solve I will want to generate a list of possible endings for N
#It is obvios that N must end in 0

#From each list of M-digit N such that
#N^2 and 1_..._9_0 have the same M digits,
#I will generate a list of (M+2)-digit N
#such that N^2 and 1_..._9_0 have the same (M+2) digits.

#I can do this enough times until I have a list of N with the correct number of digits
#Then I can check if each N^2 matches 1_2_..._9_0



#Returns answer
def Main():
    endings = [0] #list of all possible endings for N
    
    for digits in range(1,12,2): #number of digits of numbers in 'endings'
        possible=[]
        
        for front in range(100):
            for end in endings:
                
                #calculate new number and its square
                num = front * 10**digits + end
                sqr = num * num

                #if large enough, check if number is answer
                if sqr > 1020304050607080900:
                    if isAns(sqr):
                        return num

                #check that the last few digits match
                if digit(sqr,digits-1) == [0,9,8,7,6,5,4,3,2,1][ digits//2]:
                    possible.append(num)

        endings = possible
        print(len(endings),digits)

ans = Main()
print(ans, time.clock()-start)    
    

"""
Peter has nine four-sided (pyramidal) dice, each with faces numbered 1, 2, 3, 4.
Colin has six six-sided (cubic) dice, each with faces numbered 1, 2, 3, 4, 5, 6.

Peter and Colin roll their dice and compare totals: the highest total wins. The result is a draw if the totals are equal.

What is the probability that Pyramidal Pete beats Cubic Colin? Give your answer rounded to seven decimal places in the form 0.abcdefg
"""
#In this problem, any list[i] = the chance of rolling i

import time
start = time.clock()


#returns the a list where list[i] is the probability of rolling
#a sum of i from (n) (sides)-sided dice
def dice_rolls(sides,n):
    #ans and die are distributions
    ans = [1]
    die = [0] + [1/sides] * sides

    for roll in range(n):
        #calculate distributing when adding current distritbution (ans)
        #with die
        tmp = [0] * (len(die) + len(ans) - 1)

        for ind1 in range(len(ans)):
            for ind2 in range(len(die)):
                tmp[ind1 + ind2] += ans[ind1] * die[ind2]

        ans = tmp
    return ans

Colin = dice_rolls(6,6)
Peter = dice_rolls(4,9)


ans = 0
#consider possibilities where Peter > Colin
for indP in range(37):
    for indC in range(indP):
        ans += Colin[indC] * Peter[indP]

print("%0.7f"% ans , time.clock()-start )

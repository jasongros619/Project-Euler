#cipher
#card 23456789TJQKA
#let  abcdefghijklm
#num2 0123456789012

CARD="23456789TJQKA"
cipher="abcdefghijklm"



def poker(hand):
    #convert hand from CARD to letters
    for i in range(5):
        hand[i]= cipher[ CARD.index(hand[i][0]) ]+hand[i][1]
    

    #hand is in let form
    hand=sorted(hand)

    #array of card values (in num2)
    c1=cipher.index(hand[0][0])
    c2=cipher.index(hand[1][0])
    c3=cipher.index(hand[2][0])
    c4=cipher.index(hand[3][0])
    c5=cipher.index(hand[4][0])
    card=[c1,c2,c3,c4,c5]
    
    #str of suits    
    suit=hand[0][1]+hand[1][1]+hand[2][1]+hand[3][1]+hand[4][1]


    ##################################


    #is there a flush?
    isFlush=False
    if suit=="CCCCC" or suit=="DDDDD" or suit=="HHHHH" or suit=="SSSSS":
        isFlush=True

    #is there a straight?
    isStraight=0
    if c2==c1+1 and c3==c2+1 and c4==c3+1 and c5==c4+1:
        isStraight=c5

    ###how many pairs
    pairs=0
    for a in card:
        for b in card:
            if a==b:
                pairs+=1

    ##return rank tuple

    #Royal Flush
    if isFlush and isStraight==12:
        return (9,c5)
    #Straight Flush
    if isFlush and isStraight!=0:
        return (8,c5)
    #Four of a kind
    if pairs==17:
        if c1== 2:
            return (7,c4)
        else:
            return (7,c5)
    #Full House
    if pairs==13:
        if c3==c4:
            return (6,c5)
        else:
            return (6,c3)
    #Flush
    if isFlush==True:
        return (5,c5)
    #Straight
    if isStraight!=0:
        return (4,isStraight)
    #Three
    if pairs==11:
        return (3,c3)
    #Two pairs
    if pairs==9:
        return (2,c4)
    #1 pair
    if pairs==7:
        if c5==c4 or c4==c3:
            return (1,c4)
        else:
            return (1,c2)
    #High
    if pairs==5:
        return (0,c5)
        

count=0
file=open("p054_poker.txt","r")
for line in file:
    line=line.split(" ")
    h1=poker(line[:5])
    h2=poker(line[5:10])
    if h1[0]>h2[0] or (h1[0]==h2[0] and h1[1]>h2[1]):
        count+=1
    if h1[0]==h2[0] and h1[1]==h2[1]:
        print(line)

file.close()
print(count)

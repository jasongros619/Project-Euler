"""
The file, poker.txt, contains one-thousand random hands dealt to two players.
Each line of the file contains ten cards (separated by a single space): the
first five are Player 1's cards and the last five are Player 2's cards. You
can assume that all hands are valid (no invalid characters or repeated cards),
each player's hand is in no specific order, and in each hand there is a clear
winner.

How many hands does Player 1 win?
"""
def poker(hand):
    #str of cards' suits
    suit = "".join([ hand[i][0] for i in range(5)] )
    
    #arr of ints of card num values
    CARD = "23456789TJQKA"
    card = sorted([ CARD.index(hand[i][0]) for i in range(5)])

    ########Examine properties

    #Flush
    isFlush = suit in ["CCCC","SSSS","HHHH","DDDD"]

    #Straight set to either highest card in staight or 0
    for i in range(1,5):
        if card[i] != 1+card[i-1]:
            break
    isStraight = card[4] if i==4 else 0

    #Stores value in pairs. Each possible type of hand has a unique amount of
    #pairs (no pair -> 5, 1 pair -> 7, 2 pair -> 9, )
    pairs = 0
    for card1 in card:
        for card2 in card:
            if card1 == card2:
                pairs += 1

    ####### Return tuple with rank

    #Royal Flush
    if isFlush and isStraight==12:
        return (9,card[4])
    #Straight Flush
    if isFlush and isStraight!=0:
        return (8,card[4])
    #Four of a kind
    if pairs==17:
        return (7, card[2])
    #Full House
    if pairs==13:
        return (5,card[2])
    #Flush
    if isFlush==True:
        return (5,card[4])
    #Straight
    if isStraight!=0:
        return (4,isStraight)
    #Three
    if pairs==11:
        return (3,card[2])
    #Two pairs
    if pairs==9:
        return (2,card[3])
    #1 pair
    if pairs==7:
        if card[4]==card[3] or card[3]==card[2]: #if c4 is in a match
            return (1,card[3])
        else:
            return (1,card[1])
    #High
    if pairs==5:
        return (0,card[4])
        

count=0
file=open("p054_poker.txt","r")
for line in file:
    line = line.split(" ")
    hand_1 = poker(line[:5])
    hand_2 = poker(line[5:10])
    if hand_1 > hand_2:
        count+=1

file.close()
print(count)

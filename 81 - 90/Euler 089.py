def romanval(val):
    rom={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}

    ans=rom[val[-1]]
    for i in range(len(val)-1):
        a=rom[val[ i ]]
        b=rom[val[i+1]]
        ans += -a if a<b else a
    return ans


rval={"1":"I","5":"V","10":"X","50":"L","100":"C","500":"D","1000":"M"}
def torome(val):
    val=str(val)[::-1]
    while(len(val)<4):
        val=val+"0"
    d=int(val[0])
    c=int(val[1])
    b=int(val[2])
    a=int(val[3])

    hundreds = ["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"]
    tens = ["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"]
    ones = ["","I","II","III","IV","V","VI","VII","VIII","IX"]
    ans = "M" * a
    ans += hundreds[b]
    ans += tens[c]
    ans += ones[d]
    return ans
#    return "M" * a + hundreds[b] + tens[c] + ones[d]

file=open("p089_roman.txt","r")

count1=0
count2=0
for line in file:
    count1+=len( torome(romanval(line[:-1])))
    count2+=len( line[:-1])
file.close()

print(count2-count1)

def romanval(val):
    rom={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}

    ans=rom[val[-1]]
    for i in range(len(val)-1):
        a=rom[val[ i ]]
        b=rom[val[i+1]]
        if a<b:
            ans-=a
        else:
            ans+=a
    return ans


rval={"1":"I","5":"V","10":"X","50":"L","100":"C","500":"D","1000":"M"}
def torome(val):
    val=str(val)[::-1]
    while(len(val)<4):
        val=val+"0"
    d=val[0]
    c=val[1]
    b=val[2]
    a=val[3]

    ans=""
    #thousands
    for i in range(int(a)):
        ans+="M"
    #hundreds
    if b=="1":
        ans+="C"
    if b=="2":
        ans+="CC"
    if b=="3":
        ans+="CCC"
    if b=="4":
        ans+="CD"
    if b=="5":
        ans+="D"
    if b=="6":
        ans+="DC"
    if b=="7":
        ans+="DCC"
    if b=="8":
        ans+="DCCC"
    if b=="9":
        ans+="CM"
    #tens
    if c=="1":
        ans+="X"
    if c=="2":
        ans+="XX"
    if c=="3":
        ans+="XXX"
    if c=="4":
        ans+="XL"
    if c=="5":
        ans+="L"
    if c=="6":
        ans+="LX"
    if c=="7":
        ans+="LXX"
    if c=="8":
        ans+="LXXX"
    if c=="9":
        ans+="XC"
    #ones
    if d=="1":
        ans+="I"
    if d=="2":
        ans+="II"
    if d=="3":
        ans+="III"
    if d=="4":
        ans+="IV"
    if d=="5":
        ans+="V"
    if d=="6":
        ans+="VI"
    if d=="7":
        ans+="VII"
    if d=="8":
        ans+="VIII"
    if d=="9":
        ans+="IX"

    return ans

file=open("p089_roman.txt","r")

count1=0
count2=0
for line in file:
    count1+=len( torome(romanval(line[:-1])))
    count2+=len( line[:-1])
file.close()

print(count2-count1)

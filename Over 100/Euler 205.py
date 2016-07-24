pyr=[1]
sqr=[1]

def addarr(a,b):
    out=[]
    while(len(a)>len(b)):
        b.append(0)
    while(len(b)>len(a)):
        a.append(0)
    for i in range(len(a)):
        out.append( a[i]+b[i])
    return out

def roll4(score):
    r1=[0]+score
    r2=[0]*2+score
    r3=[0]*3+score
    r4=[0]*4+score

    ra=addarr(r1,r2)
    rb=addarr(r3,r4)
    rc=addarr(ra,rb)

    return rc

def roll6(score):
    r1=[0]+score
    r2=[0]*2+score
    r3=[0]*3+score
    r4=[0]*4+score
    r5=[0]*5+score
    r6=[0]*6+score

    ra=addarr(r1,r2)
    rb=addarr(ra,r3)
    rc=addarr(rb,r4)
    rd=addarr(rc,r5)
    re=addarr(rd,r6)

    return re


for i in range(9):
    pyr=roll4(pyr)

for i in range(6):
    sqr=roll6(sqr)

pwin=0
cwin=0
tie=0
for i in range(37):
    for j in range(37):
        if i==j:
            tie+=pyr[i]*sqr[j]
        elif i>j:
            pwin+=pyr[i]*sqr[j]
        elif i<j:
            cwin+=pyr[i]*sqr[j]
tot=pwin+cwin+tie
print(pwin/tot)
print(cwin/tot)
print(tie/tot)

file=open("p098_words.txt","r")
for line in file:
    arr=(line[1:-1])
arr=arr.split("\",\"")
file.close()

def rename(num):
    word=str(num)
    out=""
    lets="abcdefghijk"
    count=0

    for i in range(len(word)):
        if word[i] in word[:i]:
            ind=word.index(word[i])
            letter=lets[ind]
            out+=letter
        else:
            out+=lets[count]
            count+=1
    return out
print(rename(12341234))

#pairs contains all word pairs w/ at least 1 anagram divided by sorted letters
pairs={}
for w in arr:
    s="".join(sorted(w))

    try:
        pairs[s].append(w)
    except:
        pairs[s]=[w]
copy=dict(pairs)
for key in copy:
    if len(pairs[key])==1:
        pairs.pop(key)

#sqrs contains all sqrs w/ at least 1 anagram divided by sorted digits
sqrs={}
for i in range(1,100000): #all words with 9 or less digits
    s="".join(sorted(str(i*i)))

    try:
        sqrs[s].append(i*i)
    except:
        sqrs[s]=[i*i]
copy=dict(sqrs)
for key in copy:
    if len(sqrs[key])==1:
        sqrs.pop(key)

#keys = patterns ABC
patterns={}
for key in pairs:
    words=pairs[key]
    for a in words:
        for b in words:
            if a!=b:
                pat=rename(a+b)
                if pat not in patterns:
                    patterns[pat]=[]


#
i=0
for key in sqrs:
    nums=sqrs[key]
    for a in nums:
        for b in nums:
            if a>b:
                name=rename(str(a)+str(b))
                if name in patterns:
                    patterns[name].append(a)

for key in patterns:
    if len(patterns[key])>0:
        print(patterns[key])
maxval=0
#print(patterns)
for key in patterns:
    for val in patterns[key]:
        if val>maxval:
            maxval=val
print(maxval)

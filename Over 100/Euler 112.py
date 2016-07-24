def bouncy(n):
    up=False
    down=False
    
    last=n%10
    n=(n-last)//10
    while(n>0):
        next=n%10
        if next>last:
            up=True
        if next<last:
            down=True
        if up and down:
            return True
        last=next
        n=(n-next)//10
    return False


count=0
i=0
while( 99*i>count*100 or i==0):
    for j in range(100):
        i+=1
        if bouncy(i):
            count+=1

print(i)

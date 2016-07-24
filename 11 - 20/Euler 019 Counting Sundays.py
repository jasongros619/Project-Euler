import time
start=time.clock()

count=0
weekday=1 #1=Mon
date=1 #1=1
month=1 #1=Jan
year=1900 #

def isleap():
    if year%400==0:
        return True
    elif year%100==0:
        return False
    elif year%4==0:
        return True
    else:
        return False

def endmonth():
    if month==1 and date==31:
        return True
    if month==2:
        if isleap():
            if date==29:
                return True
        else:
            if date==28:
                return True
    if month==3 and date==31:
        return True
    if month==4 and date==30:
        return True
    if month==5 and date==31:
        return True
    if month==6 and date==30:
        return True
    if month==7 and date==31:
        return True
    if month==8 and date==30:
        return True
    if month==9 and date==31:
        return True
    if month==10 and date==31:
        return True
    if month==11 and date==30:
        return True
    if month==12 and date==31:
        return True

    return False


while(year<2000):
    if weekday==0 and date==1:
        count+=1

    if not endmonth:
        weekday=(weekday+1)%7
        date+=1
    else:
        if month==12:
            year+=1
            month=1
            date=1
            weekday=(weekday+1)%7
        else:
            month+=1
            date=1
            weekday=(weekday+1)%7

print(count,(time.clock()-start)*1000,"ms")    

z=50
red=[0,1,2]
for i in range(3,z+1):
    red.append( red[-1]+red[-2])
    #print(red[-1]-1)
print(" ")
gre=[0,1,1,2]
for i in range(4,z+1):
    gre.append( gre[-1]+gre[-3])
    #print(gre[-1]-1)
print(" ")
blu=[0,1,1,1,2]
for i in range(5,z+1):
    blu.append( blu[-1]+blu[-4])
    #print(blu[-1]-1)

print( red[50]+blu[50]+gre[50])

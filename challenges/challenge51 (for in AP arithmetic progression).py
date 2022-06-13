print('Ill read the first term and the common difference of an arithmetic progression (AP) and show you the first ten terms ')
print('-'*105)
a1 = int(input('First term : ') )
r = int(input('Common difference : '))
for c in range (1,11):
    ## general form of an AP
    t = a1 + (c- 1)*r
    print(c,'term',t)
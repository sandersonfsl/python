
l = 0
s = 0
for p in range (1, 6) :
    weight = float(input('weight of {} person '.format(p)))
    if p == 1 :
        l = weight
        s = weight
    else :
        if weight > l :
            l = weight
        if weight < s :
            s = weight

print(' The  greater weight is : {}'.format(l))
print(' The lighter weight is : {} '.format(s))
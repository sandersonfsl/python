l = []
for c in range (0,5) :
    l.append(int(input('value ')))

for c, v in enumerate(l) :
    if c == 0 :
        biggest = smallest = v
    else :
        if v > biggest :
            biggest = v
        if v < smallest :
            smallest = v

print(f'biggest value : {biggest} , smallest value : {smallest}  ')
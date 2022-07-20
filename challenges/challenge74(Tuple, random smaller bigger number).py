import random as rd
t = (rd.randint(1,10),rd.randint(1,10),rd.randint(1,10),rd.randint(1,10),rd.randint(1,10))

print(f'your list is {t} ')
print(f'list lenght : ', len(t))



for c, v in enumerate(t) :
    if c == 0 :
        bigger = smaller = v
    else :
        if v > bigger :
            bigger = v
        if v < smaller :
            smaller = v
    
print(f'bigger number = {bigger} smaller number = {smaller}')


## using max and min
## print(max(t))
## print(min(t))













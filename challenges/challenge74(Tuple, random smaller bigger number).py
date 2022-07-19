import random as rd
t = (rd.randint(1,18000),rd.randint(1,18000),rd.randint(1,18000),rd.randint(1,18000),rd.randint(1,18000))

print(f'your list is {t} ')
print(len(t))


for c, v in enumerate(t) :
    if c == 0 :
        bigger = smaller = v
    else :
        if v > bigger :
            bigger = v
        if v < smaller :
            smaller = v

print(f' Bigger Number = {bigger} , Smaller Number = {smaller}')









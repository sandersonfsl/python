import random as rd
print(' ----- MEGASENA : BIGGEST BRAZILIAN LOTTERY  ----- ')

## Making the user choice
userlist = []
print(' Pick  SIX numbers between 1 and 60 ')

for c in range (0,6) :
    n = int(input(f' Pick the {c + 1} number  : '))
    userlist.insert(c, n)

## Showing the user choice
print('The list of your Numbers : ', userlist)

## System choice 
list = list(range(1,61))
pick = rd.sample(list, k=6)
print(f'Numbers Drawn : {pick} ')

## Counting...
d = 0

for j in range(0, 6) :
    if pick[j] in userlist :
        d += 1


print(f'You got {d} number(s) right ')
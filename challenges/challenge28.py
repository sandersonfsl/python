import random as rd
a = [0,1,2,3,4,5]
c = rd.choice(a)
print(c)

choice = int(input('type a number between 0 and 5 :'))

if choice == c:
    print('You Win! ')
else:
    print('You lose ')


'''import random as rd

a = rd.randint(0,10)
count = 0
c = 11
print(a)
while a != c :
    c = int(input('Pick a number between 0 and 10 '))
    count += 1

print(' You nailed it ! ')
print(' {} tries '.format(count))'''


from random import randint
pc = randint(0,10)
guess = 0

correct = False
while not correct :
    p = int(input('whats your guess : '))
    guess += 1
    if p == pc :
        correct = True
print('You got it !! {} tries '.format(guess))





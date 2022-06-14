import random as rd

a = rd.randint(0,10)
count = 0
c = 11
print(a)
while a != c :
    c = int(input('Pick a number between 0 and 10 '))
    count += 1

print(' You nailed it ! ')
print(' {} tries '.format(count))




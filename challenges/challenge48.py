n1 = int(input('INT number 1 : '))
n2 = int(input('INT number 2 : '))
s = 0
for c in range(n1,n2,1):
    if c % 2 != 0 and c % 3 == 0:
        s = s + c
        print(c)
        

print('the sum between even numbers divisible by 3 between {} and {} is {} :'.format(n1,n2,s))
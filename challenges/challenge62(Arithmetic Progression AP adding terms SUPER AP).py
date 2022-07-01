print('____AP (Arithmetic Progression) Generator______')
print('-='*24)

a1 = int(input('First term : '))
cd = int(input('Common difference : '))
t = a1
c = 1
hm = 0
m = 10
while m != 0 :
    hm += m
    while c <= hm :
        print('{} -> '.format(t), end='')
        t += cd
        c += 1

    m = int(input('\n How many terms do you want to see ? '))

print( ' DONE ! with {} terms'.format(hm))

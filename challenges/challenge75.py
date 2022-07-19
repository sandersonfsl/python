for c in range (1,5) :
    n = int(input(' number '))
    if c == 1 :
        c1 = n*1
    if c == 2 :
        c2 = n*1
    if c == 3 :
        c3 = n*1
    if c == 4 :
        c4 = n*1

l = (c1,c2,c3,c4)
print(f'you typed {l}')

print(f'you typed 9 ,  {l.count(9)} times')

if 3 not in l :
    print('3 not typed !')
else :
    print(f'3 position is {l.index(3)+1}')


for count, value in enumerate(l) :
    if value % 2 == 0 :
        print(f'even {value}')

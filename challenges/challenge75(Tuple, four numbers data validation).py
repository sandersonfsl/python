l = (int(input('type a number ')), int(input('type a number ')), 
int(input('type a number ')), int(input('type a number ')))

print(f'you typed {l}')

print(f'you typed 9 ,  {l.count(9)} time(s)')

if 3 not in l :
    print('3 not typed !')
else :
    print(f'position of 3 :  {l.index(3)+1}')


print('Even Values : ')
for c in l :
    if c % 2 == 0 :
        print(c)

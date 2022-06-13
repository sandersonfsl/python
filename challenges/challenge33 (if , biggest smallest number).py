print('Type 3 different int numbers : ')
a = int(input(' type the first number: '))
b = int(input(' type the second number: '))
c = int(input(' type the third number: '))

if a > b and a > c and c > b :
    print('biggest ', a)
    print('smallest', b)
if a > b and a > c and b > c :
    print('biggest ', a)
    print('smallest', c)
if b > a and b > c and c > a :
    print('biggest', b)
    print('smallest', a)
if b > a and b > c and c < a :
    print('biggest ', b)
    print('smallest', c)
if c > a and c > b and b > a :
    print('biggest ', c)
    print('smallest', a)
if c > a and c > b and b < a :
    print('biggest ', c)
    print('smallest', b)









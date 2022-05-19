y = str(input('year : '))


if y[len(y)- 1] == '0' and y[len(y)- 2] == '0' and int(y) % 400 == 0 :
    print('leap year')

if int(y) % 4 == 0  :
    print('leap year')

else :
    print('common year')


## 2100 is a common year
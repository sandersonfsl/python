# To be a leap year, the year number must be divisible by four – except
# for end-of-century years, which must be divisible by 400. This means
# that the year 2000 was a leap year, although 1900 was not. 

year = input('Year ? ')

if year[-1] == '0' and year[-2] == '0':
    d = int(year) % 400
    if d == 0:
        print('Leap year')
    else :
        print('Common year')
elif int(year) % 4 == 0:
    print('Leap year')
else :
    print('Common year')

'''from datetime import date

y = int(input('type the year (if you want current year type 0 : '))

if y == 0 :
    y = date.today().year

if y % 4 == 0 and y % 100 != 0 or y % 400 == 0 :
    print(' leap year')
else :
    print('common year')'''

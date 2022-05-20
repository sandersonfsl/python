# To be a leap year, the year number must be divisible by four – except
# for end-of-century years, which must be divisible by 400. This means
# that the year 2000 was a leap year, although 1900 was not. 

y = input('Year ? ')

if y[-1] == '0' and y[-2] == '0':
    d = int(y) % 400
    if d == 0:
        print('Leap year')
    else :
        print('Common year')
elif int(y) % 4 == 0:
    print('Leap year')
else :
    print('Common year')

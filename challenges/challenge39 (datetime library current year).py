from datetime import date
y = int(input('Your year of birth : '))
cy = date.today().year

if cy - y < 18 :
    p = 18 - (cy - y)
    print('youll still enlist in {} years'.format(p))
    

elif cy - y == 18 :
    print('you must enlist in the army ')

else :
    p2 = (cy - y) - 18
    print('you are {} years late for enlistment '.format(p2))

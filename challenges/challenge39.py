from datetime import date
y = int(input('Your year of birth : '))
cy = date.today().year

if cy - y < 18 :
    print('youll still enlist')

elif cy - y == 18 :
    print('you must enlist in the army ')

else :
    print('you are late for enlistment ')
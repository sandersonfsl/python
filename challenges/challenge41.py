from datetime import date
a = int(input('Your born year : '))
print(' Your age {} '.format(date.today().year - a))

if date.today().year - a <= 9 :
    print(' junior category ')
elif date.today().year - a > 9 and date.today().year - a <= 14 :
    print(' Children category ') 
elif date.today().year - a > 14 and date.today().year - a <= 19 :
    print(' Teen category ')
elif date.today().year - a == 20 :
    print(' Senior category ') 
else :
    print(' Master category ')

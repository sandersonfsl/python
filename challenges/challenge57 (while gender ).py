g = str(input('Your gender [m/f]: ')).lower()

while g != 'm' and g != 'f' :
    g = str(input(' You must type m or f :'))

print('You are {} '.format(g))
    
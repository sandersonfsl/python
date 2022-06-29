'''g = str(input('Your gender [m/f]: ')).lower()

while g != 'm' and g != 'f' :
    g = str(input(' You must type m or f :'))

print('You are {} '.format(g))'''
    

g = str(input('your gender [M/F] : ')).strip().upper()[0]## [0] show only the first character ##
while g not in 'MmFf' :
    g = str(input(' Invalid Data , type M or F : ')).strip().upper()[0] 
print(' Your gender {}'.format(g))
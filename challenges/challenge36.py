v = float(input('Property value ? '))
s = float(input('You salary R$ ? '))
y = int(input('How many year do you want to pay ? '))
iv = v / ( y * 12 ) 
print('Installment value : R$ ', iv)

if iv > 0.3 * s :
    print('Loan Denied ')
else :
    print('Loan Granted ')

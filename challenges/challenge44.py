p = float(input(' Price ? '))
c = int(input('Payment terms ? TYPE : \n1 for cash \n2 for debit card \n3 for two installments\n4 for three installments \n '))
if c == 1 :
    print('youll pay ', p*0.90)
elif c == 2 :
    print('youll pay', p*0.95)
elif c == 3 :
    print('youll pay', p)

else :
    print('youll pay ', 1.2*p)
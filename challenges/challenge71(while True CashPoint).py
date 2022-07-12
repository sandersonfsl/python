print('=' * 30)
print('{:^30}'.format('CASHPOINT'))
print('=' * 30)


n = int(input(' CASHPOINT , US$ ? [50 dollar - 20 dollar - 2 dollar - 1 dollar] '))
total = n
bill = 50
count = 0

while True : 
    if total >= bill :
        total -= bill
        count += 1
    else :
        if count > 0 :
            print(f'total  = {count} bills of {bill}')
        if bill == 50 :
            bill = 20
        elif bill == 20 :
            bill = 10
        elif bill == 10 :
            bill = 1
        count = 0
        if total == 0 :
            break
    

















'''import math
n = int(input(' CashPoint : How much do you want ?  '))

op = math.trunc(n / 50) 

x = n - (op * 50)

if op != 0 :
    print(f'{op} notas de 50 ')

op2 = math.trunc(x/20)

if op2 != 0 :
    print(f'{op2} notas de 20')

x2 = x - (op2 * 20)

op3 = math.trunc(x2/10)

if op3 != 0 :
    print(f'{op3} notas de 10')

x3 = x2 - (op3 * 10)

op4 = math.trunc(x3/1)

if op4 != 0 :
    print(f'{op4} notas de 1')'''










 
    
    
    




    























##if a.isnumeric() == True :
    ##acount += a
    ##print(acount)



'''
a = n/100
b = n/50
c = n/20
d = n/10
e = n/5
f = n/2
g = n/1'''



'''print(a,b,c,d,e,f,g)'''


#a = b = c = d = e = f = g = 1
# n = 100*g + 50*f + 20*e + 10*d + 5*c + 2*b + 1*a

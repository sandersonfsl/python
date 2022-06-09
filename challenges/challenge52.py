print('I will read an int number and show you if it is a prime number ')
print('-'*63)
n = int(input('type an int number : '))
s = 0
for c in range (1,n+1):
    if n % c == 0:
        s = s + 1

if n != 1 :    
    if s > 2 :
        print('regular number ')
    else :
        print('prime number')
else :
    print('regular number ')
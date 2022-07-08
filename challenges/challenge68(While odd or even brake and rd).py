import random as rd

count = 0
while True :
    
    n = int(input('Choose a number (0 to 10) : '))
    c = ' '
    while c not in 'eo' :
        c = str(input('Type o for Odd,  e for Even : ')).strip().lower()[0]

    n2 = rd.randint(0,10)
    print(f'pc number = {n2}')

    if c =='o' and (n + n2) % 2 == 0 :
        print('you lose ! ')
        break

    elif c == 'e' and (n + n2) % 2 == 0 :
        print('you win !')
        count += 1

    elif c == 'o' and (n+2)%2 !=0 :
        print('you win !')
        count += 1

    elif c == 'e' and (n + n2) % 2 != 0 :
        print('you lose !')
        break

        

print(f'END with {count} wins ')



 
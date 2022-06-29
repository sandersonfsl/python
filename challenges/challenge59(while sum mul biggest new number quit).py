from time import sleep
n1 = int(input(' n 1 = '))
n2 = int(input(' n 2 = '))
c = 0


while c != 5 :

    c = int(input(' [1] sum [2] mul [3] bigger [4] new numbers [5] quit \n '))

    if c == 1 :
        sum = n1 + n2 
        print('sum : ',sum )
    elif c == 2 :
        mul = n1 * n2
        print('mul ', mul)
    elif c == 3 :
        if n1 > n2 :
            m = n1
            print('bigger ', m)
        else :
            m = n2
            print('bigger', n2)
    elif c == 4 :
        print('type 2 numbers again ')
        n1 = int(input('n1 = '))
        n2 = int(input('n2 = '))
    elif c == 5 :
        print('Exiting program ... ')
        sleep(2)

    else :
        print('Invalid option ')

print( ' Bye ! ')



'''c = 4 
while c == 4 :
    n1 = float(input(' number 1 : '))
    n2 = float(input(' number 2 : '))
    c = int(input('choice 1 sum  2 mul 3 biggest 4 new numbers and 5 quit : '))
while c == 1 :
    print(n1+n2)
    break
while c == 2 :
    print(n1*n2)
    break
while c == 3 :
    if n1 > n2 :
        print('biggest ', n1)
    else :
        print('biggest', n2)
    break
while c == 5 :
    print('BYE !')
    break '''
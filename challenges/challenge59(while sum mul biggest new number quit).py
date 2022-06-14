c = 4 
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
    break

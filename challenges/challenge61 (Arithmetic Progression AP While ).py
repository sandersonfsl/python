print('Ill read the first term and the common difference of an arithmetic progression (AP) and show you the first ten terms ')

a1 = int(input('first term : '))
cd = int(input('common difference : '))
c = 1 
t = 0
while  c <= 10 :
    t = (t - 1) + cd
    c = c + 1
    print(t)


    


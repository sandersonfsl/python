print('Ill read the first term and the common difference of an arithmetic progression (AP) and show you the first ten terms ')

a1 = int(input('first term : '))
cd = int(input('common difference : '))

t = a1
c = 1

while  c <= 10 :
    print(t)
    t += cd
    c += 1


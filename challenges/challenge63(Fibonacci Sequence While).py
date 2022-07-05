n = int(input(' how many terms : '))

t1 = 0
t2 = 1
print(f'{t1} --> {t2}', end='')
t = 2 
while t <= n :
    t3 = t1 + t2
    print(f'--> {t3} ', end='')
    t1 = t2
    t2 = t3
    t += 1


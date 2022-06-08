print(' Ill read a number and show you its multiplication table')
print('-'*70)
n = int(input('type a number  '))
for c in range(1,11,1):
    print('{} x {} = {}'.format(n,c,n*c))
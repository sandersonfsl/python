print(' Ill read six int numbers and show you the sum of these even numbers')
print('-'*70)
s = 0
for c in range(1,7):
    n = int(input(' INT number : '))
    if n % 2 == 0:
        s = s + n
print(s)
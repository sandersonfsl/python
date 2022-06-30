'''n = int(input('type a number : '))
c = n
f = 1

while c > 0 :
    print('{} '.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f)'''


''' from math import factorial
n = int(input('type a number : '))
print(factorial(n)) '''


'''n = int(input('type an int number :'))

r = 1 
c = 1 

while c <= n :
    r = r * c
    c = c + 1

print(r)'''


''' Using for
n = int(input('n : '))
s = 1

for c in range (1, n + 1) :
    s = s * c

print(s)

'''
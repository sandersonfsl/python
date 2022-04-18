##quadratic equation

print('***Quadratic Equation calculator*** ')
a = float(input('a coefficient: '))
b = float(input('b coefficient :'))
c = float(input('c coefficient: '))
delta = b**2 - 4*a*c

x1 = (-b+(delta**0.5))/2*a
x2 = (-b-(delta**0.5))/2*a
print('delta: ',delta)
print('1 Root: ',x1)
print('2 Root: ',x2)




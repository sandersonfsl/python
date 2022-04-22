## quadratic equation solver
## when discriminant = 0 there is no real root
## when discrmimant  > 0 there are two real roots
## whe discriminant < 0 there are two complex roots 
print('***Quadratic Equation solver*** ')
a = float(input('a coefficient: '))
b = float(input('b coefficient :'))
c = float(input('c coefficient: '))
discriminant = b**2 -(4*a*c)
x1 = ((-b+discriminant**0.5))/(2*a)
x2 = ((-b-discriminant**0.5))/(2*a)
print('Discriminant: ',discriminant)
print('Root 1: ', x1)
print('Root 2: ', x2)


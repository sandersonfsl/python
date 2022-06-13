import math
a = float(input('first line segment: '))
b = float(input('second line segment: '))
c = float(input('third line segment: '))

if math.fabs(b - c) < a < b + c and math.fabs(a - c) < b < a + c and math.fabs(a - b) < c < a + b :
    print('these 3 line segments CAN make a triangle ')
else :
    print('these 3 line segments CANNOT make a triangle')
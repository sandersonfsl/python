import math
a = int(input('first line segment: '))
b = int(input('second line segment: '))
c = int(input('third line segment: '))

if math.fabs(b - c) < a < b + c and math.fabs(a - c) < b < a + c and math.fabs(a - b) < c < a + b :
    print('these 3 line segments CAN make a triangle ')
else :
    print('these 3 line segments CANNOT make a triangle')
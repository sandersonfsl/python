in1 = int(input('first int number : '))
in2 = int(input('second int number: '))

print('the odd numbers between {} and {}  :'.format(in1,in2))
print("-"*40)
for c in range(in1, in2,1):
    if c % 2 == 0:
        print(c)
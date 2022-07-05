n = int(input(' type an int number [999 to stop] '))
sum = 0
c = 0
while n != 999 :
    sum += n
    c += 1
    n = int(input(' type an int number [999 to stop] '))

print(f'{c} numbers,  sum = {sum}' )
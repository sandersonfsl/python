from re import S


s = 0
for c in range(1,7):
    n = int(input('type a number '))
    if n % 2 == 0 :
        s = s + n

print(s)
num = int(input('0 to 9999 '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('unity',u)
print('ten',d)
print('hundred',c)
print('thousands',m)
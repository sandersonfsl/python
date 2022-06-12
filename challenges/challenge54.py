from datetime import date
s = 0
a = 0

for c in range(1,8) :
y = int(input('Your year of birth : '))
if date.today().year - y < 18 :
s = s + 1
elif date.today().year - y >= 18 :
a = a + 1
print('{} uder age  and {} of age  '.format(s,a))

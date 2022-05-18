n = input('whats your full name ? ')
print(n.upper())
print(n.lower())
a = n.split()
b = ''.join(a)
print('this name lenght is : ', len(b))
## OR print(len(n) - n.count(' '))
print('the first name has',len(a[0]),' characters ')




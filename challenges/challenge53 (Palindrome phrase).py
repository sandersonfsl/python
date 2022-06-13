print('Ill show if what I read is a Palindrome phrase ')
print('-'*50)

n = input('type anything ')
r = n.replace(' ','').lower().strip()

size = len(r)
a = r[0:size]
b = r[::-1]

if a == b:
    print('Palindrome')
else:
    print('Its not palindrome')

''' second method :

n = str(input('write a phrase ')).strip().upper()
p = n.split()
j = ''.join(p)
inn = ''

for l in range(len(j) -1, -1, -1):
inn = inn + j[l]

if j == inn :
print('palindrome ')
else :
print('not palindrome')
'''

n = input('type anything: ')
nmod = n.lower()

a = nmod.count('a')
print('how many a {}'.format(a))

b = nmod.find('a')
print('firt A position {}'.format(b))

c = nmod.rfind('a')
print('last A position {}'.format(c))
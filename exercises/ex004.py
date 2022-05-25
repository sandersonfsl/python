n = (input('what your name ')).lower()
if n == 'sanderson':
    print('What a beautiful name !')
elif n == 'maria' or n == 'joao' or n == 'pedro':
    print('Your name is popular ')
elif n in 'livia maria alexandre martins':
    print('What a beautiful female name !')

print('have a nice day', n)  
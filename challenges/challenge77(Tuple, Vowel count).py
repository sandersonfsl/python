
l = ('LEARN', 'PROGRAM', 'LANGUAGE', 'PYTHON', 'MACHINE', 'STUDY', 'LIBRARY',
'TUPLE', 'DICTIONARY', 'LIST')

for c in range (0, len(l)) :
    print(f'the word {l[c]} have these vowels : ', end=' ')
    if 'A' in l[c] or 'E' in l[c] or 'I' in l[c] or 'O' in l[c] or 'U' in l[c] :
        print(l[c].count('A')*'A', l[c].count('E')*'E', l[c].count('I')*'I', l[c].count('O')*'O', l[c].count('U')*'U')


for w in l :
    print(f'\nword {w} have : ', end=' ')
    for letter in w :
        if letter.lower() in 'aeiou' :
            print(f'{letter}', end=' ')




'''
for c in range (0, len(l)) :
    print(f'the word {l[c]} have these vowels : ', end=' ')
    if 'A' in l[c] or 'E' in l[c] or 'I' in l[c] or 'O' in l[c] or 'U' in l[c] :
        print(l[c].count('A')*'A', l[c].count('E')*'E', l[c].count('I')*'I', l[c].count('O')*'O', l[c].count('U')*'U')'''



'''for c in range (0, len(l)) :
    print(f'{l[c]} have : ', end=' ')

    
    if 'A' in l[c] :
        print('A', end=' ')

    if 'E' in l[c] :
        print('E', end=' ')

    if 'I' in l[c] :
        print('I', end=' ')

    if 'O' in l[c] :
        print('O', end=' ')

    if 'U' in l[c] :
        print('U', end=' ')



for c in range (0, len(l)) :
    l1 = (l[c].count('A'),l[c].count('E'), l[c].count('I'),l[c].count('O'),l[c].count('U'))'''
    
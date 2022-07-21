
l = ('LEARN', 'PROGRAM', 'LANGUAGE', 'PYTHON', 'MACHINE', 'STUDY', 'LIBRARY',
'TUPLE', 'DICTIONARY', 'LIST')

# first option
for c in range (0, len(l)) :
    print(f'the word {l[c]} have these vowels : ', end=' ')
    if 'A' in l[c] or 'E' in l[c] or 'I' in l[c] or 'O' in l[c] or 'U' in l[c] :
        print(l[c].count('A')*'A', l[c].count('E')*'E', l[c].count('I')*'I', l[c].count('O')*'O', l[c].count('U')*'U')

# sencond option
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

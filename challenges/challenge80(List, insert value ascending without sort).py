l = []

for c in range (0,5) :
    n = int(input('type a number '))
    if c == 0 or n > l[-1]:
        l.append(n)
        print('added at the end ... ')
    else :
        position = 0
        while position < len(l) :
            if n <= l[position] :
                l.insert(position, n)
                print(f'added at {position} position ...')
                break
            position += 1
print(l)


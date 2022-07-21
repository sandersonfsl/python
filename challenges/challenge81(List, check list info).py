l = []
while True :
    n = int(input('type a number '))
    o = str(input('want to continue [y/n] ? '))
    while o not in 'YyNn' :
        o = str(input('Wrong option , type [y/n] ? '))
    l.append(n)
    if o in 'Nn' :
        break
print(f'{len(l)} numbers typed ')
print(f'{sorted(l, reverse=True)} in reverse order ')
if 5 in l :
    print(f'5 was typed in {l.index(5) + 1} position ')
else :
    print('5 was not found ')
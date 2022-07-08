c1 = c2 = c3 = 0
while True :
    
    try :
        a = int(input('Person Age :'))
        while a < 0 :
            a = int(input('Invalid Data , enter a NATURAL NUMBER'))

    except ValueError :
        print('Invalid Data , enter a NATURAL NUMBER')
        continue
    

    g = str(input('Person Gender : [m/f] ')).strip().lower()[0]
    while g not in 'MmFf':
        g = str(input('Invalid data type [m/f] '))

        
    o = str(input('Want to Continue [y/n] ?')).strip().lower()[0]
    while o not in 'YyNn' :
        o = str(input('Invalid data type [y/n] '))
    
    if a > 18 :
        c1 += 1
    if g in 'm' :
        c2 += 1
    if g in 'f' and a < 20 :
        c3 += 1
    if o in 'n' :
        break
print(f'Over eighteen --> {c1} person | Male --> {c2} person | Female under twenty --> {c3} person  ')


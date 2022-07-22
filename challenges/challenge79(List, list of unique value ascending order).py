l = []
while True :
    n = int(input(' type a number : '))
    if n in l :
        print('Duplicate value , i wont add !')
    else :
        print('successfully added !')
        l.append(n)
    o = str(input(' want to continue ? [Y/N] '))
    if o in 'Nn' :
        break
    
print(f'list of unique values in ascending order : {sorted(l)}')
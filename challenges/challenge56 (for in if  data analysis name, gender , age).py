Gnolder = 0
Snolder = 0
older = ''
a = 0
b = 0
for c in range (1,5) :
    name = str(input('{} person name : '.format(c)))
    age = int(input('{} person age : '.format(c)))
    gender = str(input('{} person genre (m or f) '.format(c)))
    a += age

    
    if gender == 'm' :
        if c == 1:
            Gnolder = age
            Solder = age
            older = name

        else :
            if age > Gnolder :
                older = name
            if age < Snolder :
                older = name
    
    if gender == 'f' :
        if age < 20 :
            b += 1


print('Average age = ', a/4)
print('Older man : ', older)
print('{} women with less than 20 years old'.format(b))


 
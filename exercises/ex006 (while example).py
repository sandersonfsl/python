'''for c in range (1,21) :
    print(c)'''

''' same for using while

c = 1
while c < 21 :
    print(c)
    c += 1
print('end')'''

'''while with flag 
n = 1 
while n != 0 :
    n = int(input('Int number'))
'''

''' ask number until n
r = 's'
while r == 's' :
    n = int(input('type an int number '))
    r = str(input('continue ? [s/n] ')).lower()
'''

print('odd even numbers while you press y or n ')
n = 'y'
even = odd = 0 
while n == 'y' :
    n = int(input('type a number '))
    if n % 2 == 0 :
        even += 1
    else :
        odd += 1
    n = str(input(('Continue ? [y/n] ')))

print('you entered {} odd numbers and {} even numbers'.format(odd,even))



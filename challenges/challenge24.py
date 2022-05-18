city = input('your city name? ')
a = city.split()
b = 'san' in a[0]

if b == True :
    print('You live in a holy city! ')
else :
    print('You dont live in a holy city !')

# OR
# c = str(input('city? ')).strip()
# print(c[:5].upper() == 'SAN')
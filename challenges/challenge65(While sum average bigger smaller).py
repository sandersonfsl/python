n = int(input('Type a number : '))
f = str(input('Do you want to continue ? [Y/N] '))
c = 1
sum = n
bigger = n
smaller = n
while f in 'Yy' :
    c += 1
    n2 = int(input('Type a number : '))
    if n2 > bigger :
        bigger = n2

    if n2 < smaller :
        smaller = n2
    f = str(input('Do you want to continue ? [Y/N] '))
    sum += n2
    

    
print(f' NUMBERS -> {c}  , SUM -> {sum} , AVERAGE -> {float(sum/c)}  , BIGGER -> {bigger},  SMALLER -> {smaller}  ', end='')
    
    



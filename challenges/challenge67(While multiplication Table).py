while True :
    n = int(input('What number multiplication table do you want to see (negative number to stop) ? '))
    if n < 0 :
        break
    for c in range(1,11) :
        print(f'{c} X {n} = {c*n}') 

print(' ---- END ---- ')
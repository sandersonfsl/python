c1 = c2 = 0
while True :
    
    n = str(input('Name : ')).strip().lower()
    
     
    p = float(input('Price US$ : '))    
    c1 += p

    

    o = str(input('Continue ? [y/n] : ')).strip().lower()
    while o not in 'YyNn':
        o = str(input('INVALID DATA ! Type Y or N] : '))

    


    if p > 1000 :
        c2 += 1

    if o not in 'Yy' :
        break



print(f' sum of prices = {c1}  | prices more than 1000 {c2} | cheaper = ')

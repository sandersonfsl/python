total= tot2 = cheaper = cont = 0
cheapername = ' '
while True :
    n = str(input('Name :'))
    p = float(input('Price U$S : '))
    cont += 1
    total += p
    if p > 1000 :
        tot2 += 1
    if cont == 1 :
        cheaper = p
        cheapername = n
    else :
        if p < cheaper :
            cheaper = p
            cheapername = n

    o = ' '
    while o not in 'YN' :
        o = str(input('Want to continue ? [Y/N] ')).strip().upper()[0]
    if o == 'N' :
        break

print(' END OF THE PROGRAM ')
print(f'Total = {total:10.2f}')
print(f'over 1000 products =  {tot2:10.2f}')
print(f'Cheaper price = {cheaper:10.2f}')
print(f'Cheaper name  = {cheapername}')

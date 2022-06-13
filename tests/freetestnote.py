sum = 0
cont = 0
for c in range (1,501,2):
    if c % 3 == 0 :
        sum = sum + c
        cont = cont + 1
print(sum, cont)
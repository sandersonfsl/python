l = []

for c in range (0,5) :
    n = int(input('type a number '))
    if c == 0 :
        l.append(n)
        print(l,' added at the end of the list ')
        
    if c == 1 :
        if n < l[0] :
            l.insert(0,n)
        else :
            l.append(n)





'''
'added at the end of the list' [4]
'added at position 0' [0]
'added at position 1' [1]
'added at position 2' [2]
'added at position 3' [3]'''


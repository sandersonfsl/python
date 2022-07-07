c = 0
s = 0

while True :
    n = int(input('Type a Number (999 to stop): '))
    if n == 999 :
        break
    c += 1
    s += n

print(f'{c} numbers  ,  sum ---> {s}')
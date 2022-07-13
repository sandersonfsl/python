'''COLOR EXAMPLE 

n = int(input('n u m b e r : '))
sum = 0
for c in range (1, n + 1) :
    if n % c == 0 :
        print('\033[34m', end = ' ')
        sum += 1
    else :
        print('\033[m', end = ' ')
    print('{} '.format(c) , end = ' ')

print('\n\033[mThe number {} was divisible {} time (s)'.format(n,sum))

if sum == 2 :
    print('Prime number ', end = ' ')
else :
    print('Regular number ', end = ' ' ) '''

'''greater lighter  weight
g = 0
l = 0

for c in range (1,6):
    w = float(input('w '))
    if c == 1 :
        g = w
        l = w
    else :
        if w > g :
            g = w

        if w < l :
            l = w

print('G ', g)
print('L', l)
'''

'''Analise de dados nome idade sexo

somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for p in range (1, 5) :
    print('--------- {}a PESSOA ----------'.format(p))
    nome = str(input('Nome : ')).strip()
    idade = int(input('Idade :'))
    sexo = str(input('Sexo [M/F] : ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome 
    if sexo in 'Mm' and idade > maioridadehomem :
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20 :
        totmulher20 += 1

mediaidade = somaidade / 4
print('A media de idade do grupo eh de {} anos '.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}'.format(maioridadehomem, nomevelho))
print('Ao todo sao {} mulheres com menos de 20 anos'.format(totmulher20)) '''

''' SUPER AP
a1 = int(input('1 term '))
cd = int(input('common difference '))
t = a1
c = 1
more = 10
m = 0

while more != 0 :
    m += more
    while c <= m :
        print(t)
        t += cd
        c += 1
    more = int(input('how many more terms ? '))

print(' DONE ! ')
'''    


''' MEDIA, MAIOR , MENOR WHILE com S e N challenge64(While sum average bigger smaller)
r = 'S'
soma = quant = maior = menor = 0

while r in "Ss" :
    
    n = int(input('type a number : '))
    r = str(input('want to continue ? [s/n] ')).upper().strip()
    soma += n
    quant += 1
    if quant == 1 :
        maior = menor = n
    else :
        if n > maior :
            maior = n

        if n < menor :
            menor = n
    
media = soma / quant

print(f'qnt --> {quant} media --> {media}  maior --> {maior} menor --> {menor} ')'''

'''print('CHALLENGE 70')
total = tot2 = cheaper = cont = 0
cheapername = ' '
while True :
    n = str(input('Name :'))
    p = float(input('Price US$ :'))
    total += p
    cont += 1 

    if cont == 1 :
        cheaper = p
        cheapername = n
    else :
        if p < cheaper :
            cheaper = p
            cheapername = n

    if p >1000 :
        tot2 += 1
    o = ' '
    while o not in 'YN' :
        o = str(input(' Continue ? ')).strip().upper()[0]

    if o == 'N' :
        break

print( ' SUM ', total)
print( ' 1000 + value = ', tot2)
print(' Cheaper value and product name ' ,cheaper, cheapername, )

'''
print('TUPLES in PYTHON')
lanche = ('hamburguer','pizza','suco','pudim')


print(lanche)
print(lanche[0])
print(lanche[-2])
print(lanche[1:3])
print(lanche[2:])
print(len(lanche))

for c in range (0, len(lanche)) :
    print(lanche[c])

print(sorted(lanche))

a = (2,5,4)
b = (5,8,1,2)
c = b + a

print(c.index(5, 1))
print(c.count(2))
print(c.count(5))
print(c.count(9))
print(c.index(8))


print('LIST IN PYTHON')

values = [1,2,3,4,5]

values.append(5)

print(values)

values.insert(0,5)

print(values)

del values[3]

print(values)

values.pop(3)

print(values)

values.remove(1)

print(values)

if 2 in values :
    values.remove(2)

print(values)

values2 = list(range(4,11))

print(values2)

values2.sort()

print(values2)

values2.sort(reverse=True)

print(values2)

print(len(values2))
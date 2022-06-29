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



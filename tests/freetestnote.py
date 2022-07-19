## AUTO GIT git add . && git commit -m "" && git push


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

'''print('TUPLES in PYTHON')
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

'''
'''
a = [2,3,4,7]

b = a[:]

b[2] = 8

print(a)

print(b)


print('Listas Compostas')

dados = list()

dados.append('Pedro')

dados.append(25)

pessoas = list()

pessoas.append(dados[:])

print(pessoas)

print(pessoas[0][1])
'''
'''
test = list()
test.append('gustavo')
test.append('40')
galera = list()
galera.append(test[:])
test[0] = 'maria'
test[1] = 22
galera.append(test[:])
print(galera)


surfers = [['toledo',29],['ferreira',27],['pupo',31],['slater',51]]

for o in surfers :
    print(o[0] , o[1])


surfers = list()
data = list()

for c in range (0,3) :
    data.append(str(input('surfer name : ')))
    data.append(int(input('surfer age : ')))
    surfers.append(data[:])
    data.clear()

print(surfers)

'''

'''
print('DICTIONARY')

pessoas = {'nome':'Gustavo', 'sexo':'M', 'idade':22}
print(f'o {pessoas["nome"]} tem {pessoas["idade"]} anos ')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())

for k in pessoas.values() :
    print(k)

brasil = []
estado1 = {'uf':'Rio de Janeiro', 'sigla' : 'RJ'}
estado2 = {'uf': 'Sao Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)

print(brasil)


estado = dict()
brasil = list()
for c in range (0,3) :
    estado['uf'] = str(input('unidade federativa'))
    estado['sigla'] = str(input('Sigla do estado : '))
    brasil.append(estado.copy())
print(brasil)
'''

'''
print('FUNCOES')

def mostralinha() :
    print('---------------------')


mostralinha()


def titulo(txt) :
	print('-'*30)
	print(txt)
	print('-'*30)

titulo('  CURSO EM VIDEO PYTHON ')
titulo(' PYTHON ' )
titulo('OI')

def soma(a,b) :
	print(f'A = {a} e B = {b}')
	s = a + b
	print(f'A soma A + B = {s}')

soma(b = 4, a = 5)

def contador(*num) :
	print(num)

contador(2,1,7)
contador(8,0)
contador(4,4,7,6,2)

v = [2,4,6,8,10,12]

'''
'''
v = [2,4,6,8,10,12]

def double(v) :
    var = 0
    for c in range (1, var) :
        v[var] = v[var] * 2
        var += 1

double(v)
print(v)


##EMPACOTAMENTO
def soma(*valores) :
    s = 0
    for num in valores :
        s += num
    print(f'somando os valores {valores} temos {s}')

soma(5,2)
soma(2,9,4)
'''


'''

### SOMA DE INFINITOS NUMEROS
def soma(x) :
    s = 0
    for c in x :
        s += c
    print(s)

l = []
while True :
    a = int(input(' type  a number [999] to end ' ))
    if a == 999 :
        break
    l.append(a)


soma(l)


## DOBRAR VALORES
def dobra(lst) :
    pos = 0
    while pos < len(lst) :
        lst[pos] = lst[pos]*2
        pos +=1

valores = [6,3,5,4,2,1]
dobra(valores)
print(valores)






def contador(i,f,p):
    i = inicio da contagem
    f = fim da contagem
    p = passo da contagem
    return : sem retorno """
    c = i
    while c <= f:
	    print(f'{c}', end='')
	    c+=p
	    print('FIM!')

contador(0,100,10)



'''
'''
## DOCSTRING
def somar(a,b,c=0) :
	""" SOMAS DE TRES VALORES 
	a = primeiro valor
	b = segundo valor
	c = terceiro valor
	"""
	s = a + b + c
	print(f'SOMA = {s} ')

somar(3,2)

'''

##SCOPE OF VARIABLES

'''
def test() :
    x = 8
    print(f'test function : n = {n}')
    print(f'test function : x = {x}')

# main program
n = 2 
print(f'main program : n = {n}')
print(f'main program : x = {x}')

test()
'''
'''
def test2(b) :
    global a
    a = 8
    b += 4
    c = 2
    print(f'A inside is {a}')
    print(f'B inside is {b}')
    print(f'C inside is {c}')

a = 5
test2(a)
print(f'A fora vale {a}')

'''

'''
#RETURN
def sum(a=0, b=0, c=0) :
    s = a + b + c
    return s

print(sum(2,4,6))
print(sum(3,2,5))
print(sum(2,2))
print(sum(6))

def my_function(x) :
	return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))


def factorial(num = 1) :
    f = 1
    for c in range (num, 0, -1) :
        f *= c
    return f


n = int(input('type a number : '))
print(f'{n} factorial = {factorial(n)}')


def evenorodd(x) :
    if x % 2 == 0:
        return True
    else :
        return False

n = int(input('type a number '))
if evenorodd(n) == True :
    print('EVEN')
else :
    print('ODD ')

'''



'''
def factorial(n) :
    f = 1
    for c in range (1,n+1) :
        f *= c
    return f

num = int(input('type an int number '))
fact = factorial(num)
print(f'{num} FACTORIAL = {fact}')

'''


## ERROR TREATMENT

try :
    a = int(input(' value 1 '))
    b = int(input(' value 2 '))
    r = a / b
except (ValueError, TypeError) :
    print('data type error ')
except ZeroDivisionError :
    print('cannot divide by 0')
except KeyboardInterrupt :
    print('user did not type')
except Exception as error :
    print(f'ERROR : {error.__cause__}')
else :
    print(r)
finally : 
    print('see u later')
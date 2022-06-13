import random as rd
a = ['r','p','s']
b = rd.choice(a)
print('PC choice :', b)

c = input('type r for Rock , p for Paper or s for Scissors ').lower()

if b == 'r' and c == 'p' :
    print('You WIN ! ')
elif b == 'r' and c == 's' :
    print('PC WIN ! ')
elif b == 'p' and c == 'r' :
    print('PC WIN ! ')
elif b == 'p' and c == 's' :
    print('You WIN ! ')
elif b == 's' and c == 'r' :
    print('You WIN ! ')
elif b == 's' and c == 'p' :
    print('PC WIN ! ')
else :
    print(' DRAW')

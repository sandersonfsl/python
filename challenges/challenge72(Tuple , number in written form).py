wf = ('zero','one', 'two', 'three','four','five','six', 'seven', 'eight','nine','ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen','twelve')

n = int(input('Type a number between 0 and 20 '))
while n < 0 or n > 20 :
    n = int(input('ERROR ! Type a number between 0 and 20 '))
print(f'{n} is {wf[n]}')
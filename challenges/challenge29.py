v = int(input('whats the speed of the car ? '))
if v>80:
    print('you were fined and you must pay US$ {:.2f}'.format((v-80)*7))
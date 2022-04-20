km = float(input('How many kilometers did you travel: '))
d = float(input('For how many days was it rented: ' ))
p = d * 60 + 0.15 * km
print('The rental price was US$ {:.2f} '.format(p))
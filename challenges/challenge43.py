w = float(input('your weight ? '))
h = float(input('your height ? '))
bmi = w / ( h ** 2 )
print('your BMI ', bmi)

if bmi < 18.5 :
    print('severe thinness ')
if bmi >= 18.5 and bmi < 25 :
    print('normal')
if bmi >= 25 and bmi < 30 :
    print(' Overweight ')
if bmi >= 30 and bmi < 40 :
    print(' Obese ')
if bmi >= 40 :
    print('morbid obesity ')

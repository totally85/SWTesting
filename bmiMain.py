import bmiCalc

weight = int(input('enter weight in pounds: '))
height = int(input('enter height in inches: '))

bmi = bmiCalc.bmi_calc(weight, height)
sort = bmiCalc.bmi_sort(bmi)

print('Your bmi is:', bmi, 'This is:', sort)

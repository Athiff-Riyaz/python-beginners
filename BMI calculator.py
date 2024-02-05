weight=float(input('what is your weight?(kg)'))
height=float(input('what is your height?(mtr)'))
bmi=(float(weight/(height*height)))

if bmi<=18.5:
    print('your BMI is', bmi,'which means you are underweight')

elif 18.5<bmi<25:
    print('your BMI is', bmi,'which means you are normal')

elif 25<bmi<30:
    print('your BMI is', bmi,'which means you are obesity')
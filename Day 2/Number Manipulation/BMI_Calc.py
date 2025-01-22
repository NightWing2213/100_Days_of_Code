print("Welcome to the BMI Calculator")
height = int(input("How tall are you in inches?"))
weight = int(input("How much do you weigh?"))
bmi=((weight / (height ** 2)) * 703)
print("Your BMI is " + str(bmi))
if(bmi<18.5):
    print("You are underweight")
elif(bmi>=18.5 and bmi < 25):
    print("Your weight is normal")
elif(bmi>=25 and bmi < 30):
    print("You are overweight")
else:
    print("You are obese")
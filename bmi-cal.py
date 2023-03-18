# BMI = weight ÷ height^2
# Weight is measured in kilograms
# Height is measured in metres.

weight = float(input("Enter your weight: "))

height = float(input("Enter your height: "))

bmi = round(weight / (height**2),2) 

print("Your BMI is {}".format(bmi))

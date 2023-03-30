# File name: bmi_cal.py
# Purpose: Calculate BMI( Body Mass Index )

while True:
    try:
        # prompt user for name
        name = str( input( "Enter your name: " ) )

        # prompt user for age 
        age = int( input( "Enter your age: " ) )

        while age > 100 or age < 13:
            print("You're not that old, try again...")
            # prompt user for age again 
            age = int( input( "Enter your age: " ) )

        # prompt user for weight in kilograms
        weight = float( input( "Enter your weight in kilogram: " ) )

        # prompt user for height in meters(m)
        height = float( input( "Enter your height in meters: " ) )
        break
    except Exception as errors:
        print('Try again...')
        print(errors)

# function that calculate bmi 
def bmi( height, weight ):
    ''' Calculates bmi '''
    return weight / ( height * height )

# display user information
# name, age, weight, height and bmi
print( "\nHello, " + name.lower().title() )
print( "Here is your results\n" )
print( "Name: " + name.lower().title() )
print( "Age: " + str(age) + " years old" )
print( "Weight: " + str(weight)+ "kg" )
print( "Height: " + str(height)+ "m")
print( "BMI:", "{:.1f}".format(bmi(height,weight)) + "\n" )

# Analysing data given by the user and
# display the result
if bmi(height, weight) < 18.5:
    print( "You are Underweight!" )
elif 18.5 <= bmi(height,weight) <= 24.9:
    print( "You are Normal!, Well Done!" )
elif 25.0 <= bmi(height,weight) <= 29.9:
    print( "You are Overweight!" )
if  bmi(height,weight) >= 30.0:
    print( "You are Obese!" )

# display the bmi value for comparison
print( "\n*********** BMI VALUES ************\n" +
       "* Underweight: less than 18.5     *\n*" +
       " Normal: between 18.5 and 24.9   *\n*" +
       " Overweight: between 25 and 29.9 *\n*" +
       " Obese: 30 or greater            *\n" +
       "***********************************" )

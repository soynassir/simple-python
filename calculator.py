''' This program is a simple calculator that will ask user to enter
    two numbers and an operation(+,-,/,*) '''
number1 = int(input("Enter a first number: ")) # ValueError
number2 = int(input("Enter a second number: "))

operation = input("Enter an operation(+,-,/,*): ")

if operation == "+":
    answer = number1 + number2
    print("{} + {} = {}".format(number1,number2,answer))
elif operation == "*":
    answer = number1 * number2
    print("{} * {} = {}".format(number1,number2,answer))
elif operation == "/":
    answer = number1 / number2
    print("{} / {} = {}".format(number1,number2,answer))
elif operation == "-":
    answer = number1 - number2
    print("{} - {} = {}".format(number1,number2,answer))
else:
    print("You haven't entered the right operator!")



''' This program is a simple calculator that will ask user to enter
    two numbers and an operation(+,-,/,*) '''
number1 = int(input("Enter a first number: "))
number2 = int(input("Enter a second number: "))

operation = input("Enter an operation(+,-,/,*): ")

users_history = 'calculator_data.txt'

# Save the user input and the answer to the txt file
with open(users_history, 'a') as data_file:
    if operation == "+":
        answer = number1 + number2
        data_file.write("{} + {} = {}\n".format(number1, number2, answer))
    elif operation == "*":
        answer = number1 * number2
        data_file.write("{} * {} = {}\n".format(number1, number2, answer))
    elif operation == "/":
        answer = number1 / number2
        data_file.write("{} / {} = {}\n".format(number1, number2, answer))
    elif operation == "-":
        answer = number1 - number2
        data_file.write("{} - {} = {}\n".format(number1, number2, answer))
    else:
        print("You haven't entered the right operator!")

read_data = open(users_history, 'r')
print(read_data.read())
read_data.close()



#Basic Calculator Program

#Create a simple Python program that asks the user to input two numbers and a mathematical operation 
# (addition, subtraction, multiplication, or division).
#Perform the operation based on the user's input and print the result.
#Example: If a user inputs 10, 5, and +, your program should display 10 + 5 = 15.


print("Hello. Welcome to the Basic Calculator Program")

try:
    # Prompt user for input
    num1 = float(input("Please enter the first number: "))  
    num2 = float(input("Please enter the second number: "))
    operation = input("Please enter the operation you would like to perform (+, -, *, /): ")

    # Perform calculation
    if operation == '+':
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")
    elif operation == '-':
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")
    elif operation == '*':
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
            print(f"{num1} / {num2} = {result}")
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Invalid operation. Please enter one of +, -, *, or /.")

except ValueError:
    print("Error: Invalid input. Please enter numeric values.")

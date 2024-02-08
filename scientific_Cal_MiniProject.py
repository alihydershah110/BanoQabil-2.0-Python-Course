# Ali Hyder Shah
# Scientific Calculator mini project

import math

# Function to add two numbers
def add(x, y):
    return x + y

# Function to subtract two numbers
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function to divide two numbers, handling division by zero
def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    else:
        return x / y

# Function to calculate the factorial of a number
def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x-1)

# Function to calculate the cosine of a number (in radians)
def cosine(x):
    return math.cos(x)

# Function to calculate the sine of a number (in radians)
def sine(x):
    return math.sin(x)

# Function to calculate the power of a number
def power(x, y):
    return x ** y

# Function to calculate the square root of a number
def square_root(x):
    return math.sqrt(x)

# Main calculator function
def calculator():
    print("Welcome to the Scientific Calculator!")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Factorial")
    print("6. Cosine")
    print("7. Sine")
    print("8. Power")
    print("9. Square Root")
    print("10. Quit")

    while True:
        # Get user input for operation choice
        choice = input("Enter choice (1/2/3/4/5/6/7/8/9/10): ")

        # Perform the selected operation
        match choice:
            case '1':
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                print("Result:", add(num1, num2))
            case '2':
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                print("Result:", subtract(num1, num2))
            case '3':
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                print("Result:", multiply(num1, num2))
            case '4':
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                print("Result:", divide(num1, num2))
            case '5':
                num = int(input("Enter a number: "))
                print("Result:", factorial(num))
            case '6':
                num = float(input("Enter a number in radians: "))
                print("Result:", cosine(num))
            case '7':
                num = float(input("Enter a number in radians: "))
                print("Result:", sine(num))
            case '8':
                num1 = float(input("Enter base: "))
                num2 = float(input("Enter exponent: "))
                print("Result:", power(num1, num2))
            case '9':
                num = float(input("Enter a number: "))
                print("Result:", square_root(num))
            case '10':
                print("Thank you for using the calculator!")
                return
            case _:
                print("Invalid input. Please enter a valid option.")

# Call the calculator function to start the program
calculator()

import math

task = input("Select action: +, -, *, /, root(\), pow(^) ")

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

match task:
    case "+":
        print("Result: ", num1 + num2)
    case "-":
        print("Result: ", num1 - num2)
    case "*":
        print("Result: ", num1 * num2)
    case "/":
        print("Result: ", num1 / num2)
    case "\\":
        print("Result: ", math.sqrt(num1), math.sqrt(num2))
    case "^":
        print("Result: ", num1 ** num2)
    case _:
        print("Incorrect action.")
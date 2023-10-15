import math
task = input("Виберіть дію: +, -, *, /, корінь(\), степінь(^) ")
num1 = int(input("Введіть перше число: "))
num2 = int(input("Введіть друге число: "))
match task:
    case "+":
        print("Результат: ", num1 + num2)
    case "-":
        print("Результат: ", num1 - num2)
    case "*":
        print("Результат: ", num1 * num2)
    case "/":
        print("Результат: ", num1 / num2)
    case "\\":
        print("Результат: ", math.sqrt(num1), math.sqrt(num2))
    case "^":
        print("Результат: ", num1 ** num2)
    case _:
        print("Неправильна дія.")
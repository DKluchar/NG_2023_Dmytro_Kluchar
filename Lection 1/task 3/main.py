gradus = int(input("Enter the degree to translate: "))

CorF = int(input("Convert from degrees Celsius or Fahrenheit? Celsius - 1, Fahrenheit - 2: "))
if CorF == 1:
    print("Celsius:", (gradus * 9 / 5) + 32)
elif CorF == 2:
    print("Fahrenheit:", (gradus - 32) * 5 / 9)
else:
    print("Incorrect number.")
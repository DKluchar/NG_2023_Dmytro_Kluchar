import math

#ax^2 + bx +c = 0
#D = b^2 - 4 * (a * c)
#x = -b +- sqrt(D) / 2 * a

print("Enter coefficients for the equation ax^2 + bx +c = 0")

a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
D = b ** 2 - 4 * (a * c)

if D > 0:
    x1 = (-b + math.sqrt(D)) / (2 * a)
    x2 = (-b - math.sqrt(D)) / (2 * a)
    print("The roots of the equation are equal to: ", x1, x2)
elif D == 0:
    x = -b / (2* a)
    print("The root of the equation is equal to: ", x)
else:
    print("An equation without roots.")
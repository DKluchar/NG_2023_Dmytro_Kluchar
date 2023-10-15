import math
#ax^2 + bx +c = 0
#D = b^2 - 4 * (a * c)
#x = -b +- sqrt(D) / 2 * a
print("Введіть коефіцієнти для рівняння ax^2 + bx +c = 0")
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
D = b ** 2 - 4 * (a * c)
if D > 0:
    x1 = (-b + math.sqrt(D)) / (2 * a)
    x2 = (-b - math.sqrt(D)) / (2 * a)
    print("Корені рівняння дорівнюють: ", x1, x2)
elif D == 0:
    x = -b / (2* a)
    print("Корінь рівняння дорівнює: ", x)
else:
    print("Рівняння немає коренів.")
import math
eps = 1.0E-3

def Eq(x, y):
    return abs(x - y) < eps

def F(x):
    return x**2 - 2

a = float(input("Введите начало интервала: "))
b = float(input("Введите конец интервала: "))

if F(a) * F(b) > 0:
    print("На этом интервале мы не можем найти решение уравнения.")
else:
    while not Eq(a, b):
        c = (a + b) / 2
        if F(c) > 0:
            b = c
        else:
            a = c
    print("Результат:", a)




def solve_quadratic_equation(a, b, c):
    discriminant = b ** 2 - 4 * a * c

    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return root1, root2
    elif discriminant == 0:
        root = -b / (2 * a)
        return root
    else:
        real_part = -b / (2 * a)
        imaginary_part = math.sqrt(abs(discriminant)) / (2 * a)
        root1 = complex(real_part, imaginary_part)
        root2 = complex(real_part, -imaginary_part)
        return root1, root2
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


def find_value_first(n):
    y = 1 - (1/2)
    for i in range(3,n+1):
        y *= (1 -(1/i))

    return y

# print(find_value_first(6))


def find_value_second(n,x):
    y = math.sin(x)
    for i in range(2,n+1):
        y+=math.sin(x**i)

    return y

# print(find_value_second(6,4))

def find_value_third(x):
    return abs(x) + x**4


# print(find_value_third(3))
def find_values_fourth(x):
    return abs(x)+ 4 * (x**3) -7*(x**2)

print(find_values_fourth(1))
def approximate_values_of_infinite_sums():
    y = 0
    for i in range(1,11):
        y += 1/(i * (i+1))
    return f'approximate values of infinite sums: {y}'

print(approximate_values_of_infinite_sums())


def approximate_values_of_infinite_sums_second():
    y = 0
    for i in range(1,11):
        y += 1/(i * (i+2))
    return f'approximate values of infinite sums: {y}'

print(approximate_values_of_infinite_sums_second())

def approximate_values_of_infinite_sums_third():
    y = 0
    for i in range(1,11):
        y += 1/(i * (i+1) * (i+2))
        return f'approximate values of infinite sums: {y}'
print(approximate_values_of_infinite_sums_third())
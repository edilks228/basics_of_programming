# import math
# a = int(input('введите число: '))
# b = math.factorial(a)
# print(b)

# a = int(input('введите число: '))
# for i in range(a-1):
#     a = a * (i + 1)
#     print(a)


def f(n):
    if n == 1:
        return 1
    else:
        return n * f(n-1)

print(f(5))
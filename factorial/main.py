# import math
# a = int(input('введите число: '))
# b = math.factorial(a)
# print(b)

a = int(input('введите число: '))
for i in range(a-1):
    a = a * (i + 1)
    print(a)

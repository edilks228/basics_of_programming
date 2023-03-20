n = int(input('введите натуральное число: '))

i = 1
while True:
    i = i + 1
    if i > n//2 or n % i == 0:
        break
if i > n // 2:
    print(f'число {n} простое')
else:
    print(f'число {i} первый делитель числа {n}')

# a = [1,2,3,4]
# b = [5,2,7,8]
# c = a + b
# d = sorted(c)
# print(d)

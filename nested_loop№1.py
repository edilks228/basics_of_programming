# n, k = map(int, input('введите два числа: ').split())
n = int(input('введите число: '))
s = 0
for i in range(n):
    y = 1
    for j in range(n):
        y = y*i
        s = s+y

print(f'ответ: {s}')



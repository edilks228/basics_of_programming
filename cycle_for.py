n = int(input('введите целое число, не больше 9999: '))
m = n
r = 0

for i in range(4):
    r = r * 10 + m % 10
    m = m // 10

if r == n:
    print('ДА')

else:
    print('НЕТ')
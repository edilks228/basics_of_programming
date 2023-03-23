n = int(input('введите число: '))
s = n
while s > 9:
    k = s
    s = 0
    while True:
        s = s + k % 10
        k = k // 10
        if k == 0:
            break
print(f'цифровой корень числа {n} равен: {s}')
a = int(input('введите число: '))
x = int(input('введите число x: '))

one = a % 10
dec = (a // 10) % 10
sum = one + dec

if sum > 9:
    print('сумма его чисел является двухзначным числом!')

if sum > x:
    print('сумма цифр больше числа x')

if sum % 6 == 0:
    print('сумма цифр кратна 6')

if dec > one:
    print('цифра десятков больше едениц ')

if one == 5:
    print('число оканчивается на 5')

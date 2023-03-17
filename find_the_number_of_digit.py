n = int(input('введите целое число'))
m = n
number_of_digit = 0
sum_of_digit = 0
while m != 0:
    number_of_digit = number_of_digit+1
    sum_of_digit += m % 10
    m = m // 10
    if m < 9 and m > 0:
        print(f'первая цифра числа: {m}')
print(f'количество цифр в числе: {number_of_digit}')
print(f'сумма всех цифр равна: {sum_of_digit}')
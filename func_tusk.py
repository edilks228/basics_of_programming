a,b,c,d = map(int,input('введите 4 чисел через запятые: ').split())
sum_biggest = []
def sum(n):
    one = n % 10
    dec = (n//10) % 10
    hun = n // 100
    rez = one + dec + hun
    return rez

def first_numb(n):
    one = 0
    while n // 10 != 0:
        n = n // 10
    print(n)
    return n

def num_of_div(n):
    rez = 0
    div = 1
    for i in range(n):
        if n % div == 0:
            rez += 1
        div += 1
    print(rez)
    return rez


def sum_div(n):

    rez = 0
    div = 1
    for i in range(n):
        if n % div == 0:
            rez += div
        div += 1

    return rez

print('суммой цифр равны:')
a_sum = sum(a)
print(a_sum)
b_sum = sum(b)
print(b_sum)
c_sum = sum(c)
print(c_sum)
d_sum = sum(d)
print(d_sum)


print('первые числа равны: ')
a_first_numb = first_numb(a)
b_first_numb = first_numb(b)
c_first_numb = first_numb(c)
d_first_numb = first_numb(d)


print('количество делителей:')
a_num_of_div = num_of_div(a)
b_num_of_div = num_of_div(b)
c_num_of_div = num_of_div(c)
d_num_of_div = num_of_div(d)

print('сумма всех делителей: ')
a_sum_div = sum_div(a)
print(f'числа {a}: {a_sum_div}')
b_sum_div = sum_div(b)
print(f'числа {b}: {b_sum_div}')
c_sum_div = sum_div(c)
print(f'числа {c}: {c_sum_div}')
d_sum_div = sum_div(d)
print(f'числа {c}: {d_sum_div}')


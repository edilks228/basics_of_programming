a,b,c,d = map(int,input('введите 4 чисел через запятые: ').split())

def sum(n):
    one = n % 10
    dec = (n//10) % 10
    hun = n // 100
    rez = one + dec + hun
    return rez

def first_numb(n):
    one = n % 10
    return one

def num_of_div(n):
    rez = 0
    div = 1
    for i in range(n):
        if n % div == 0:
            rez += 1
        div += 1

    return rez


def sum_div(n):

    rez = 0
    div = 1
    for i in range(n):
        if n % div == 0:
            rez += div
        div += 1

    return rez

a_sum = sum(a)
b_sum = sum(b)
c_sum = sum(c)
d_sum = sum(d)
if a_sum > b_sum:
    print(a_sum)




a = int(input('введите чему будет равно a: '))
b = int(input('введите чему будет равно b: '))
c = int(input('введите чему будет равно c: '))


while a == 0 or b == 0:
    if a > b:
        a = a % b
    else:
        b = b % a

print(f'НОД :{a+b}')

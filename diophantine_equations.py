a = int(input('введите чему будет равно a: '))
b = int(input('введите чему будет равно b: '))
c = int(input('введите чему будет равно c: '))


while True or False:
    if a > b:
        a = a % b
    else:
        b = b % a
    if a == 0 or b == 0:
        break
print(f'НОД :{a,b}')
print('что за хрень просиходит ')
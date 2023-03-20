a,b = map(int,input('введите числа >0 через пробел: ').split())
while True:
    if a>b:
        a = a % b
    else:
        b = b % a
    if a == 0 or b == 0:
        break
print(f'НОД :{a+b}')
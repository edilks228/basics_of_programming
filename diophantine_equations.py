a = int(input('введите чему будет равно a: '))
b = int(input('введите чему будет равно b: '))
c = int(input('введите чему будет равно c: '))


while a == 0 or b == 0:
    if a > b:
        a = a % b
    else:
        b = b % a
<<<<<<< HEAD

print(f'НОД :{a+b}')
=======
    if a == 0 or b == 0:
        break
print(f'НОД :{a,b}')
>>>>>>> 280e8823e1a1307969106b013b0cd25744fc506f

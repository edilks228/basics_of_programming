x = int(input('введите чему будет равен x. 1 = True или 0 = False: '))
y = int(input('введите чему будет равен y. 1 = True или 0 = False: '))

if x == 1:
    x = True
elif x == 0:
    x = False
else:
    print('1 = True или 0 = False')

if y == 1:
    y = True
elif y == 0:
    y = False
else:
    print('1 = True или 0 = False')


a = x | y
b = not(x) or not(y)

if a == b:
    print('x|y эквивалентен not(x) or not(y)')

else:
    print('x|y не эквивалентен not(x) or not(y)')

print(x)
print(y)
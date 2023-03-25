n = int(input('введите число: '))
k = int(input('введите второе число: '))
a = []
b = 0
s = 0
pos = 0
neg = 0
zero = 0
for i in range(n):
    b += 1
    a.append(b)

    if a[i] % k == 0:
        s = s+a[i]

    if a[i] > 0:
        pos+=1
    elif a[i]< 0:
        neg+=1
    elif a[i] == 0:
        zero+=1

    while i >=1 and a[i]>0:
        i-=1
        if i<1:
            print('отрицательных значений в массиве нет')
        else:
            print(f'последний отрицательный элемент имеет номер: {i}')

print(a)
print(f'sum of multiply {k}: {s}')
print(f'quantity of positive numbers: {pos}')
print(f'quantity of negative numbers: {neg}')
print(f'quantity of zero numbers: {zero}')

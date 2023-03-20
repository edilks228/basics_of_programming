# mersenne part
num = int(input('введите число: '))
mersenne = 2**num-1
print(f'mercone number = {mersenne}')

#prime part
i = 1
while True:
    i = i + 1
    if i > mersenne//2 or mersenne % i == 0:
        break
if i > mersenne // 2:
    print(f'число {mersenne} простое')
else:
    print(f'число {i} первый делитель числа {mersenne}')
#2

import random
a = int(input('введите число a: '))
b = int(input('введите число b: '))
sum = 0
sum_of_interval = 0
n = 10
quantity_of_odd = 0
neg = 0
array = []
for i in range(n):
    num = random.randint(-99, 99)
    array.append(num)
for j in array:
    if j>a:
       sum+=j

    elif a<j<b:
        sum_of_interval += j

    elif j%2 != 0:
        quantity_of_odd +=1

    elif j < 0:
        neg+=1
biggest_num = max(array)
print(f'sum: {sum}')
print(f'sum of interval: {sum_of_interval}')
print(f'quantity of odd: {quantity_of_odd}')
print(f'negative number: {neg}')
print(array)
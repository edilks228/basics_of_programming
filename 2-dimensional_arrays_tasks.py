# given 2-d array. find in every column quantity and sum of elements :
"""create array"""
m = int(input('m: ')) #4
n = int(input('n: ')) #4

array = [[0] * m for _ in range(n)]
number = 1
for i in range(n):
    for j in range(m):
        array[i][j] = number
        number+=1

print(array)
a = int(input('a: '))#2
b = int(input('b: '))#5

# 1. multiple a or b
sum_of_multiple_array = []
quantity_array = []
for j in range(m):
    sum_of_multiple = 0
    quantity = 0
    for i in range(n):
        if array[i][j] % a == 0 or array[i][j] % b == 0:
            sum_of_multiple+=array[i][j]
            quantity+=1
    sum_of_multiple_array.append(sum_of_multiple)
    quantity_array.append(quantity)

print(f'sum: {sum_of_multiple_array}, quantity: {quantity_array}')
# out: sum: [5, 32, 15, 40], quantity: [1, 4, 1, 4]


# 2. in range from a to b
sum_of_range_array = []
quantity_range_array = []
sum_of_range = 0
quantity = 0
for j in range(m):
    sum_of_range = 0
    quantity = 0
    for i in range(n):
        if a < array[i][j] and array[i][j]<b:
            sum_of_range+=array[i][j]
            quantity+=1
    sum_of_range_array.append(sum_of_range)
    quantity_range_array.append(quantity)
print(f'sum: {sum_of_range_array}, quantity: {quantity_range_array}')
# out: sum: [0, 0, 3, 4], quantity: [0, 0, 1, 1]

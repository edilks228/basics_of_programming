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


#3. Given two square arrays A and B. Print the one
# whose trace is smaller (the sum of the elements of the main diagonal)
def sum_diogonal(A,B):
    A_diogonal_sum = 0
    for i in range(len(A)):
        for j in range(len(A[0])):
            if j == i:
                A_diogonal_sum += A[i][j]
    B_diogonal_sum = 0
    for i in range(len(B)):
        for j in range(len(B[0])):
            if j == i:
                B_diogonal_sum += B[i][j]
    return max(A_diogonal_sum, B_diogonal_sum)
array_2 = [[1, 5, 6, 2], [3, 2, 5, 1], [3, 1, 12, 15], [11, 15, 18, 16]]

print(sum_diogonal(array,array_2))# out: 34

# 4. given 2d array. define:
# №1.is there any negative number
# №2.is there same number
# №3.is there given number A among the elements
negative_numb = False
same_numb = set()
same_numb_bool = False
A_number = False
for i in range(n):
    for j in range(m):
        if array[i][j] < 0:
            negative_numb = True
        if array[i][j] in same_numb:
            same_numb_bool = True
        same_numb.add(array[i][j])
        if array[i][j] == a:
            A_number = True
print(f'any negative numbers = {negative_numb} same number = {same_numb_bool} A among the elements = {A_number}')
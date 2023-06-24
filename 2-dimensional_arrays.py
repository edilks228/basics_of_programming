# 1
# Fill array A with size n*m in the form of a snake
m = int(input('m: '))
n = int(input('n: '))

array = [[0] * m for _ in range(n)]
number = 1
for i in range(n):
    if i % 2 == 0:
        for j in range(m):
            array[i][j] = number
            number+=1
    else:
        for j in range(m-1,-1,-1):
            array[i][j] = number
            number += 1

print(array)
# out: [[1, 2, 3, 4],
#       [8, 7, 6, 5],
#       [9, 10, 11, 12],
#       [16, 15, 14, 13]]

# Form arrays A according to the following rules:
# A = [[1, 0, 2, 0, 3, 0, 4],
#      [0, 5, 0, 6, 0, 7, 0] and so on

counter = 1
is_previous_zero = False
for i in range(n):
    for j in range(m):
        if not is_previous_zero:
            array[i][j] = counter
            counter += 1
            is_previous_zero = True
        else:
            array[i][j] = 0
            is_previous_zero = False
print(array)
# out: [[1, 0, 2, 0],
#       [3, 0, 4, 0],
#       [5, 0, 6, 0],
#       [7, 0, 8, 0]]


# B = [[1, 8, 9, 16],
#      [2, 7, 10, 15],
#      [3, 6, 11, 14],
#      [4, 5, 12, 13]]

number = 1
for j in range(m):
    if j % 2 == 0:
        for i in range(n):
            array[i][j] = number
            number+=1
    else:
        for i in range(n-1,-1,-1):
            array[i][j] = number
            number += 1

print(array)
# out: [[1, 8, 9, 16],
#       [2, 7, 10, 15],
#       [3, 6, 11, 14],
#       [4, 5, 12, 13]]

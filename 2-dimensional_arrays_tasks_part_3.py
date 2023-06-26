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


'''№1. need to insert string with 0 after string with t-number'''
t = int(input('t: '))  # t = 1
def after_t_numb(t,array):
    for i in range(n):
        for j in range(m):
            if array[i][j] == t:
                for colun in range(m):
                    if i + 1 >= n:
                        array.append([0] * m)
                        break
                    else:
                        array[i+1][colun] = 0
    print(array)
# out: [[1, 2, 3, 4],
#       [0, 0, 0, 0],
#       [9, 10, 11, 12],
#       [13, 14, 15, 16]]

'''№2. need to insert string with 0 after string max number'''
def after_max(array):
    max_numb_string = max(array)
    max_numb_elem = max(max_numb_string)
    for i in range(n):
        for j in range(m):
            if array[i][j] == max_numb_elem:
                for colun in range(m):
                    if i + 1 >= n:
                        array.append([0] * m)
                        break
                    else:
                        array[i + 1][colun] = 0
    print('add string with 0 after max numb')
    return array

# print(after_max(array))

# out: [[1, 2, 3, 4],
#       [5, 6, 7, 8],
#       [9, 10, 11, 12],
#       [13, 14, 15, 16],
#       [0, 0, 0, 0]]


''' №3. delete string with t-number'''
def delete_t(t,array):
    string_index = []
    for i in range(n):
        for j in range(m):
            if array[i][j] == t:
                string_index.append(i)
    for i in string_index:
        del array[i]
    print('delete string with t-number')
    return array
# print(delete_t(t,array))

# out: [[5, 6, 7, 8],
#       [9, 10, 11, 12],
#       [13, 14, 15, 16]]



''' №4. delete string with max number'''
def delete_max(array):
    max_numb_string = max(array)
    max_numb_elem = max(max_numb_string)
    string_index = []
    for i in range(n):
        for j in range(m):
            if array[i][j] == max_numb_elem:
                string_index.append(i)
    for i in string_index:
        del array[i]
    print('delete string with max number')
    return array
# print(delete_max(array))
# out: [[1, 2, 3, 4],
#       [5, 6, 7, 8],
#       [9, 10, 11, 12]]


''' №5. Swap the elements of columns with numbers l1 and l2.'''
l1 = int(input('l1: ')) #l1 = 2
l2 = int(input('l2: ')) #l2 = 3
def swap_columns(l1,l2):
    for row in array:
        row[l1], row[l2] = row[l2], row[l1]
    print('Swap the elements of columns with numbers l1 and l2')
    return array
# print(swap_columns(l1,l2))

#out: [[1, 2, 4, 3],
#       [5, 6, 8, 7],
#       [9, 10, 12, 11],
#       [13, 14, 16, 15]]


"""delete string and column with max number"""
def delete_string_column_max(array):
    max_column = []
    max_string = []
    max_numb_string = max(array)
    max_numb_elem = max(max_numb_string)
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] == max_numb_elem:
                max_column.append(j)
                max_string.append(i)

    sorted(max_column)
    sorted(max_string)
    for i in max_string:
        del array[i]

    for j in max_column:
        for i in range(len(array)):
            del array[i][j]
    print('delete string and column with max number')
    return array

print(delete_string_column_max(array))
#out: [[1, 2, 3],
#       [5, 6, 7],
#       [9, 10, 11]]


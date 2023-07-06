'''given array A = [10,5,11,-5,1,-4,13,12,-4,13]'''

A = [10,5,11,-5,1,-4,13,12,-4,13]
indexes = []
for i in range(len(A)):
    count = 0
    for j in range(len(A)):
        if A[i] > A[j]:
            count+=1
        if A[i] == A[j] and i > j:
            count+=1
    indexes.append(count)
# print(indexes)
sorted_array = list(range(len(A)))

j = 0
for i in range(len(A)):
    elem = A[i]
    index = indexes[j]
    sorted_array[index] = elem
    j+=1

# print(sorted_array)

'''sort by even numbers'''
def Insertion_sort_by_even(array):
    even_num = []
    even_index = []
    for i in range(len(array)):
        if array[i] % 2 == 0:
            even_index.append(i)
            even_num.append(array[i])

    for i in range(len(even_num)):
        for j in range(i+1, len(even_num)):
            if even_num[i] > even_num[j]:
                even_num[i],even_num[j] = even_num[j], even_num[i]

    for i in range(len(even_index)):
        array[even_index[i]] = even_num[i]

    return array


arr = [3, 8, 1, 6, 2, 9, 4, 7]

# print(Insertion_sort_by_even(arr))

'''given array [12,3,5,7,9,10] for 1 iteration it will be sorted. exclude superfluous iterations '''
source_array = [12,3,5,55,7,9,10,11,33]
def Exchange_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(0,n-i-1):
            if array[j] > array[j+1]:
                array[j],array[j+1] = array[j+1],array[j]
        break

    return array
# print(Exchange_sort(source_array))


''' change view direction reversal the first -> and the second <-. 
alternate these directions until we get sorted array'''
def Exchange_sort_reverse(array):
    n = len(array)
    for i in range(n//2):
        # first direction --->
        for j in range(len(array)-1):
            if array[j] > array[j+1]:
                array[j],array[j+1] = array[j+1],array[j]

        # second direction <---
        for j in range(len(array)-1,0,-1):
            if array[j] < array[j-1]:
                array[j],array[j-1] = array[j-1],array[j]

    return array
# print(Exchange_sort_reverse(source_array))

'''sorting 5 elements in 7 comparisons'''

def sort_five_elem(array):
    if array[0] > array[1]:
        array[0], array[1] = array[1], array[0]

    if array[2] > array[3]:
        array[2], array[3] = array[3], array[2]

    if array[1] > array[3]:
        array[1], array[3] = array[3], array[1]
        array[0], array[2] = array[2], array[0]

    if array[4] < array[1]:
        if array[4] < array[0]:
            array[4], array[3] = array[3], array[4]
            array[3], array[1] = array[1], array[3]
            array[1], array[0] = array[0], array[1]
        else:
            array[1], array[4] = array[4], array[1]
            array[3], array[4] = array[4], array[3]
    else:
        if array[4] < array[3]:
            array[4], array[3] = array[3], array[4]
        if array[2] <array[1]:
            if array[2] < array[0]:
                array[1], array[2] = array[2], array[1]
                array[0], array[1] = array[1], array[0]
            else:
                array[1], array[2] = array[2], array[1]
        else:
            if array[2] > array[3]:
                array[2], array[3] = array[3], array[2]

    return array

print(sort_five_elem([5,4,3,2,1]))







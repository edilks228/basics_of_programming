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
print(indexes)
sorted_array = list(range(len(A)))

j = 0
for i in range(len(A)):
    elem = A[i]
    index = indexes[j]
    sorted_array[index] = elem
    j+=1

print(sorted_array)

'''sort by even numbers'''
def insertion_sort_by_even(array):
    for i in range(1,len(array)):
        if array[i] % 2 == 0:
            key = array[i]
            j = i - 1
            while j >= 0 and array[j] > key and array[j]%2 == 0:
                array[j+1] = array[j]
                j-=1
            array[j+1] = key
    return array



arr = [4, 9, 2, 6, 5, 7, 8, 1, 3]

print(insertion_sort_by_even(arr))


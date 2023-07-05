'''sorting by simple selection'''

source_array = [5, 13, 7, 9, 1, 8, 16, 4, 10, 2]
def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr

# print(selection_sort(source_array))

'''exchange sorting algorithm'''
def exchange_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(0,n-i-1):
            if array[j] > array[j+1]:
                array[j],array[j+1] = array[j+1],array[j]

    return array
# print(exchange_sort(source_array))

'''insertion sort'''

def insertion_sort(array):
    for i in range(1,len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key:
            array[j+1] = array[j]
            j-=1
        array[j+1] = key
    return array
# print(insertion_sort(source_array))

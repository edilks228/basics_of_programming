'''binary search'''

def binary_search(array, target):
    low = 0
    high = len(array)-1
    find_target = False
    while low <= high and not find_target:
        middle = (low+high)//2
        guess = array[middle]

        if guess == target:
            find_target = True
            return find_target
        elif guess < target:
            low = middle + 1
        else:
            high = middle - 1
    return find_target


# print(binary_search([1,3,5,7,9],7))

'''sort array by frequency elem'''

def sort_by_frequensy(A,array_of_elem):
    search_freq = {}
    for i in array_of_elem:
        for j in A:
            if j == i:
                if i in search_freq:
                    search_freq[i] +=1
                else:
                    search_freq[i] = 1

    sorted_A = sorted(A, key=lambda x: -search_freq.get(x,0))
    return sorted_A

A = [5,2,8,3,2,5,8,2,1]
array_of_elem = [2,5,8,1]
# print(sort_by_frequensy(A, array_of_elem))

'''given array and number x:'''
# 1. rearrange the elements of the array so that at the beginning there are
# numbers less than or equal to x and at the end greater than

def rearrange_by_X(array, x):
    out = []
    for i in array:
        if i <= x:
            out.insert(0,i)

        elif i >= x:
            out.insert(-1,i)
    return out
array_rearange = [5,3,4,8,1,3,6,83,4,5,1,29,1]
print(rearrange_by_X(array_rearange,5))

# 2.  rearrange the elements of the array so that at the beginning there are
# numbers less than x, in the middle equal to x and at the end greater

def rearrange_by_X2(array, x):
    left = 0
    right = len(array)-1
    i = 0
    while i <= right:
        if array[i] < x:
            array[i],array[left] = array[left], array[i]
            left+=1
            i+=1
        elif array[i]>x:
            array[i],array[right] = array[right],array[i]
            right-=1
        else:
            i+=1
    return array

# print(rearrange_by_X2(array_rearange,5))

'''given an array of N distinct integers. Allowed operations are the addition of two arrau elem 
and sum comparison. find the largest elem i array minimum number of comparisons '''

def find_max_number(array):
    first_max = array[0]
    secon_max = array[0]
    sum = 0
    for i in range(len(array)-1):
        for j in range(i, len(array)):
            current_sum = array[i] + array[j]
            if current_sum > sum:
                sum = current_sum
                first_max = array[i]
                secon_max = array[j]
    if first_max > secon_max:
        return first_max
    else:
        return secon_max

array_numbers = [1,2,3,10,5,6,7,8,9]
# print(find_max_number(array_numbers))

'''let X[1..N], Y[1..N] - two ascending order arrays. find middle elem 
sets taken from associations of two arrays'''

def find_middle_elem(X,Y):
    leftX = 1
    rightX = len(X)-1
    leftY = 1
    rightY = len(Y)-1
    while leftX < rightX and leftY < rightY:
        midX = (leftX + rightX)//2
        midY = (leftY + rightY)//2
        if X[midX] <= Y[midY]:
            leftX = midX
            rightY = midY
        else:
            leftY = midY
            rightX = midX
    if X[rightX] <= Y[rightY]:
        return X[rightX]
    else:
        return Y[rightY]

X = [1,3,5,7,9]
Y = [2,4,6,8,10]
print(find_middle_elem(X,Y))




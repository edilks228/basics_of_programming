# input: nums = [0,1,0,3,12]
# output: [1,3,12,0,0]

nums = [0,1,0,3,12]
num = []
zero = []
def zeroSort(A):
    if A == []:
        return 0
    elif A[0] == 0:
        zero.append(A[0])
    else:
        num.append(A[0])
    return zeroSort(A[1:])


zeroSort(nums)
output = num + zero

print(output)
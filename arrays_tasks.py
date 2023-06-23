# FIRST TASK!!
# change:
array = [1,2,3,4,-5,-6,7,8,9,-10,55,66]
# №1. replace elements from k1-th to k2-th with opposite signs;
if array[1] < 0:
    array[1] = abs(array[1])
if array[1] > 0:
    array[1] = -abs((array[1]))

if array[2] < 0:
    array[2] = abs(array[2])
if array[2] > 0:
    array[2] = -abs((array[2]))
print(array)
 # out: [1, -2, -3, 4, -5, -6, 7, 8, 9, -10, 55, 66]


array = [1,2,3,4,-5,-6,7,8,9,-10,55,66]
# №2. first negative number to zero:
first_neg_num = False
for i in range(len(array)):
    if array[i] < 0 and not first_neg_num:
        first_neg_num = True
        array[i] = 0

print(array) # out: [1, 2, 3, 4, 0, -6, 7, 8, 9, -10, 55, 66]

# №3. max number to opposite num
array = [1,2,3,4,-5,-6,7,8,9,-10,55,66]
max_num = array[0]
mux_num_index = 0
for i in range(len(array)):
    if array[i] > max_num:
        max_num = array[i]
        mux_num_index = i
if max_num < 0:
    array[mux_num_index] = abs(array[mux_num_index])
if max_num > 0:
    array[mux_num_index] = -abs(array[mux_num_index])
print(array) # out: [1, 2, 3, 4, -5, -6, 7, 8, 9, -10, 55, -66]

# №4. numbers that multiple 5 to zero
array = [1,2,3,4,-5,-6,7,8,9,-10,55,66]
first_multiple_num = False
for i in range(len(array)):
    if array[i] % 5 == 0 and not first_multiple_num:
        first_multiple_num = True
        array[i] = 0
print(array) # out: [1, 2, 3, 4, 0, -6, 7, 8, 9, -10, 55, 66]

# №5. replace odd-numbered elements with their squares numbers
array = [1,2,3,4,-5,-6,7,8,9,-10,55,66]
for i in range(len(array)):
    if array[i] % 2 != 0:
        array[i] = pow(array[i],2)
print(array) # out: [1, 2, 9, 4, 25, -6, 49, 8, 81, -10, 3025, 66]

# №6. the last positive number to second elem
array = [1,2,3,4,-5,-6,7,8,9,-10,55,66]
last_positive_index = 0
for i in range(len(array)):
    if array[i] > 0:
        last_positive_index = i

array[last_positive_index] = array[1]
print(array) # out: [1, 2, 3, 4, -5, -6, 7, 8, 9, -10, 55, 2]

# №7. all elements between max and min
array = [1,2,3,4,-5,-6,7,8,9,-10,55,66]
array.sort()
for i in range(1,len(array)-1):
    array[i] = 0
print(array) # out: [-10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 66]

# №8. all elements multiple 3 to third elem
array = [1,2,3,4,-5,-6,7,8,9,-10,55,66]
for i in range(len(array)):
    if array[i] % 3 == 0:
        array[i] = array[2]
print(array) # out: [1, 2, 3, 4, -5, 3, 7, 8, 3, -10, 55, 3]

# №9. all odd indexes numbers divide without reminder for first elem
# here I change first elem to other bc my first elem is 1(
array = [3,2,3,4,-5,-6,7,8,9,-10,55,66]
for i in range(len(array)):
    if i % 2 != 0:
        array[i] = array[i] // array[0]

print(array) # out: [3, 0, 3, 1, -5, -2, 7, 2, 9, -4, 55, 22]


# SECOND TASK!!!!
# insert number t:
# №1. after every element multiple itself index
k = int(input('enter k: ')) #k = 5
array = [3,2,3,4,-5,-6,7,8,9,-10,55,66]
out = []
for i in range(len(array)):
    out.append(array[i])
    if i % array[i] == 0:
        out.append(k)
print(out) #out: [3, 5, 2, 3, 4, -5, -6, 7, 8, 9, -10, 55, 66]

# №2. before every 1 number
array = [2,3,4,5,1,2,1,2,3,1]
out = []
for i in range(len(array)):
    if array[i] == 1:
        out.append(k)
    out.append(array[i])
print(out) # out = [2, 3, 4, 5, 5, 1, 2, 5, 1, 2, 3, 5, 1]


# №3. after first neg num
array = [3,2,3,4,-5,-6,7,8,9,-10,55,66]
first_neg_number = False
out = []
for i in range(len(array)):
    out.append(array[i])
    if array[i] < 0 and not first_neg_number:
        first_neg_number = True
        out.append(k)

print(out)










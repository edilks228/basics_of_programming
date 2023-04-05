# //1,2,3,4,5,6
#
# //1,2,3
# //4,5,6
#
# //1,4,2,5,3,6

MyArray = [1, 2, 3, 4, 5, 6]
a = []
b = []

for i in MyArray:
    if i > len(MyArray)/2:
        b.append(i)
    else:
        a.append(i)

print(a)
print(b)

c = []


for e in range(len(a)):
    c.append(a[e])
    c.append(b[e])

print(c)

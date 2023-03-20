# mine solution


# stroka = str(input('введите римские цифры: '))
# number = []
# for i in stroka:
#     if i == 'I':
#         number.append(1)
#     if i == 'V':
#         number.append(5)
#     if i == 'X':
#         number.append(10)
#     if i == 'L':
#         number.append(50)
#     if i == 'C':
#         number.append(100)
#     if i == 'D':
#         number.append(500)
#     if i == 'M':
#         number.append(1000)
#
# a = 0
# for b in number:
#     a += b
#
# print(a)
#

# solution that I found in internet
b = str(input('введите римское число: '))
a ={
    'I':1,
    'V':5,
    'X':10,
    'L':50,
    'C':100,
    'D':500,
    'M':1000
}

num = 0
for i in b:
    num += a[i]
print(num)
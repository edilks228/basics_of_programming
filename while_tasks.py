# n = int(input('введите натуральное число: '))
# print(n)
# while n != 1:
#     if n % 2 == 0:
#         n = n // 2
#     else:
#         n = (3 * n + 1) // 2
#     print(f'-{n}')

a = 1
b = 1
k = 0
while a+b<8:
    k += 1
    a = a+1
    b = b+2
s = a + b

print(k)
print(s)
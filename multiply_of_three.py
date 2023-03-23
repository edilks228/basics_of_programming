n = int(input('введите число: '))
m = n*3
print(f'm: {m}')
while True:
    s = 0
    t = m
    while m > 0:
        q = m % 10
        s = s+q*q*q
        m = m // 10
    m = s
    print(f'm: {m}')
    if m == t:
        break
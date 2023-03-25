f = 10
for n in range(f+1):
    for m in range(f+1):
        for k in range(f+1):
            if n ** 2 + m ** 2 == k ** 2:
                print(n,m,k, 'прикинь они есть')

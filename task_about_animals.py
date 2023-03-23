for b in range(10):
    for k in range(20):
        t = 100-(b+k)
        if 20*b+10*k+t == 200 and b+k+t == 100:
            print(f'быков: {b}, коров: {k}, телят: {t}')



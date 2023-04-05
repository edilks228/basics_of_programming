def Nod(a,b):
    while True:
        if a>b:
            a = a % b

        elif b > a:
            b = b % a

        elif a == 0 or b == 0:
            break

    Nod = a+b
    return Nod

print(Nod(16,24))
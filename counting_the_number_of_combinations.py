def Fact(numb):
    for i in range(numb-1):
        numb = numb * (i+1)
    return numb



n,m = map(int,input('введите числа n и m: ').split())

c = Fact(n) / (Fact(m)*Fact(n-m))
print(c)
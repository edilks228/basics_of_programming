a,b,c = map(int,input().split())
def Swap(a,b,c):
    if a>b:
        a,b, = b,a
    elif b>c:
        b,c = c,b
    elif a>b:
        a,b = b,a
    print(a,b,c)
Swap(a,b,c)

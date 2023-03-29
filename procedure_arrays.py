from random import randint

n = 8
l = -10
h = 21
MyAray = [0]*n
A = MyAray


def init (t,v,w:int,x:MyAray):
    i = 1
    for i in range(t):
        x[i] = v + randint(0,w)
def Print(t:int,x:MyAray):
    i = int
    for i in range(t):
        print(x[i])

print('формирование значений элементов массива A')
init(n, l, h, A)
print(n, A)

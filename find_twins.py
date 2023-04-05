from random import randint
n = 10
la = -10
ha = 21
m = 8
lb = -15
hb = 31
MyArray = [0]*n
A = MyArray
B = MyArray
C = MyArray
k = 0
def init (t,v,w:int,x:MyArray):
    i = 1
    for i in range(t):
        x[i] = v + randint(0,w)
def Solve(qx, qy:int,qz:int, X:MyArray,Y:MyArray, Z:MyArray):
    i =1
    j = 1
    # qz = 0
    for i in range(qx):
        for j in range(qy):
            if X[i] == Y[j]:
                # qz = qz+1
                Z[qz] = X[i]
                qz = qz + 1

init(n, la, ha, A)
print('вывод значений элементов массива A')
print(n, A)
init(m, lb, hb, B)
print('вывод значений элементов массива B')
print(m, B)
Solve(n, m, k, A, B, C)
print('вывод тех чисел, которые есть и в A, и в B')
print(k,C)

# проблема которую нужно решить:
# list assignment index out of range(массив вышел за границы на 25 строке)
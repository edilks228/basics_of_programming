# def Degree(x:int,y:int,st):
#     # st = 1
#     for i in range(y):
#         st = st*x
#
# q,d,n,x = map(int, input().split())
# s = 0
# t = n
# w = 1
# for i in range(n+1):
#     Degree(x,t,w)
#     s = s+q*w
#     t = t-1
#     q = q+d
# print(f'результат: {s}')



q, d, n, x = map(int, input('enter numbers separated by space: ').split())

def Divide(q,d,n,x):
    val = 0
    while n > 0:
        val += q*x**n
        q += d
        n -= 1
    print(val)

Divide(q,d,n,x)
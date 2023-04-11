# factorial with recursion
def factorial(n):
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)

# print(factorial(5))


# two sum with recursion
def two_sum(a,b):
    if b == 0:
        return a
    elif b > 0:
        return two_sum(a+1, b-1)
    else:
        return two_sum(a-1,b+1)

# print(two_sum(3,2))



# from decimal to binary

def Rec(n):
    if n > 1:
         Rec(n//2)
         print(n % 2)
# Rec(10)

# is number prime number
# def Simple(m,n):
#     if m == n:
#         return True
#     else:
#         Simple(n % m != 0) and Simple(m+1,n)

# print(Simple(2,45656))



# to find greatest commin divisor
def Nod(a,b):
    if a == 0 or b == 0:
        return a+b
    else:
        if a>b :
            return Nod(a-b, b)
        else:
            return Nod(a,b-a)

# print(Nod(12, 24))

# finding max of global array

A = [12,34,5,3,45,6,78,4,99]
def Search_Max(n,x):
    if n ==1:
        return A[1]
    else:
        Search_Max(n-1,x)
        if A[n] > x :
            return A[n]
# print(Search_Max(2,5))

# reverse number
# n = int(input(''))
def Solve():
    if n!=0:
        Solve()
        return print(n/5)
# print(Solve())

# Fibonachi number

def Fib(n):
    if n<=2:
        return 1
    else:
        return Fib(n-1)+Fib(n-2)
print(Fib(6))

# finding the sum of the first terms of an arithmetic progression

def Sa(n,a,d):
    if n>0:
        return a+Sa(n-1, a+d)
    else:
        return 0

print(Sa(5,1,1))
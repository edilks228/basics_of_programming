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
        return Rec(n//2)
    print(n % 2)
"""i dont think that it correct cause it always return 1 :( """
Rec(5)
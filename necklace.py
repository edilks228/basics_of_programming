print('this program find how many different necklace can be made')
n = int(input('enter the number: '))


def factotial(n):
    for i in range(n-1):
        n = n * (i + 1)
    return n


def necklace(a,n):
    rez = (n/a)/2
    return rez

fac_num = factotial(n)

print(necklace(n, fac_num))
# №1: change the program to find out the sum of two numbers:
a = int(input('введите первое число: '))
b = int(input('введите второе число: '))
rez = a + b
print(rez)


# №2: change the program to find out the sum of four numbers:
a, b, c, d = map(int,input('введите числа через побелы: ').split())
rez = a + b + c + d
print(rez)


# №3: find the value of expression (a+(d-12)*3)*(c-5*k),
#where values of varibles a,d,c,k are entered from the keyboar:
a, d, c, k = map(int,input('введите числа через побелы: ').split())
rez = (a + (d - 12) * 3) * (c - 5 * k)
print(rez)


# №4 write a program that displays several numbers on the screen in the form:
# 13
#    14
#        15
#            15
#                16
a = [13,14,15,16]
b = ' '
for i in a:
    print(b,i)
    b = b + '   '
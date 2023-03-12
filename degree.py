# r1 = 2
# r2 = r1 * r1                        #4
# r3 = r2 * r1                        #8
# r4 = r2 * r2                        #16
# r5 = r1 * r1 * r1 * r1 * r1         #32
# r6 = r3 * r3                        #64
# r7 = r3 * r4                        #128
# r8 = r4 * r4                        #256
# r9 = r3 * r3 * r3                   #512
# r10 = r2 * r2 * r2 * r2 * r2        #1024

#Modify program My3_1 to calculate the power of a triple

# r1 = 3
# r2 = r1 * r1
# r3 = r2 * r1
# r4 = r2 * r2
# r5 = r1 * r1 * r1 * r1 * r1
# r6 = r3 * r3
# r7 = r3 * r4
# r8 = r4 * r4
# r9 = r3 * r3 * r3
# r10 = r2 * r2 * r2 * r2 * r2
#
# print(r10)

#Modify program My3_2 so that it performs the conversion of decimal numbers
# from a certain interval to the ternary number system and vice versa.


a = int(input('введите число меньше 256 больше 128: '))
if 256 > a > 128:
    b = ''
    while a > 3:
        b = str(a % 3) + b
        a = a // 3

    print(b)

else:
    print('ВВЕДИТЕ число МЕНЬШЕ 256 БОЛЬШЕ 128')
'''write a function to find:'''
# yesterday's date

def yesterdays_date():
    date = input('enter date')
    date_array = date.split('.')
    day = int(date_array[0])
    month = int(date_array[1])
    year = int(date_array[2])


    thirty_days = [30, 4, 6, 9, 11]

    thirty_one_days = [31, 1, 3, 5, 7, 8, 10, 12]

    if year % 4 != 0:
        lenth_of_feb = [28,2]
    else:
        lenth_of_feb = [29, 2]

    if day-1 <=0:
        month -= 1
        if month - 1 <= 0:
            month = 12
            year -= 1
        if month in thirty_days:
            day = thirty_days[0]
        elif month in thirty_one_days:
            day = thirty_one_days[0]
        else:
            day = lenth_of_feb[0]

            if month-1 <=0:
                month = 12
                year-=1

    return [day,month,year]


# print(yesterdays_date())

# determine the date that was m days before the specified date

from datetime import datetime, timedelta
def day_before_m(date_str, m):
    date = datetime.strptime(date_str,'%Y-%m-%d')
    delta = timedelta(days=m)
    new_date = date - delta
    new_date_str = new_date.strftime('%Y-%m-%d')
    return new_date_str


'''write a program to find angle in radians a(vector) task on a p.223 picture.1.20'''
import math
def find_angle(w):
    v = math.sqrt(w.x**2 + w.y**2)

    if v == 0:
        return 0

    else:
        if w.x == 0:
            if w.y > 0:
                angle = math.pi/2

            else :
                angle = 3 * math.pi/2

        else:
            if w.y == 0:
                if w.x > 0:
                    angle = 0
                else:
                    angle = math.pi
            else:
                angle = math.atan(abs(w.y / w.x))
                if w.x * w.y > 0:
                    if w.x < 0:
                        angle = math.pi + angle

                else:
                    if w.x < 0:
                        angle = math.pi / 2 + angle
                    else:
                        angle = 2 * math.pi - angle
    return angle

class Tpoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y

w = Tpoint(4,4)
print(find_angle(w))

'''find scalar'''
v = Tpoint(3,3)
def find_scalar(w,v):
    return v.x * w.x + v.y * w.y

# print(find_scalar(w,v))

""" the procedure for calculating the coefficientsn in the equation 
of a straight linepassing through two points"""

class Tpoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Tline:
    def __init__(self, A, B, C):
        self.A = A
        self.B = B
        self.C = C

def Point2TwoLine(A,B,L):
    L.A = B.y - A.y
    L.B = A.x - B.x
    L.C = -(A.x * L.A + A.y * L.B)

def line2ToPoint(fL,sL,P):
    st = fL.A *sL.B - sL.A * fL.B
    if st !=0:
        P.x = -(fL.C * sL.B - sL.C * fL.B) / st
        P.y = -(sL.A * fL.C - fL.A * sL.C) / st
        return True
    else:
        return False


A = Tpoint(0,8)
B = Tpoint(-4,4)
L = Tline(0,0,0)
P = Tpoint(0,0)

Point2TwoLine(A,B,L)
if line2ToPoint(L, L, P):
    print("координаты точки пересечения:", P.x, P.y)
else:
    print("прямые паралленльны")



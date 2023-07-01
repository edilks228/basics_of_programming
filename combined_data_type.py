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


print(yesterdays_date())

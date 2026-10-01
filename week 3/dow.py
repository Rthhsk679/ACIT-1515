month_index = [1, 4, 4, 0, 2, 5, 0, 3, 6, 1, 4, 6]
dotw_index = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
offset_index = [6, 4, 2, 0, 6, 4]
day_overflow = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def getoffset(year):
    offset = (year % 1600) // 100
    return offset

def getDayOfTheWeek(year, month, day, offset):
    decade = year % 100

    step1 = decade // 12
    step2 = decade % 12
    step3 = step2 // 4
    step5 = month_index[month - 1]

    leap_adjustment = 0

    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        if month <= 2:
            leap_adjustment = -1

    result = (step1 + step2 + step3 + day + step5
              + offset_index[offset] + leap_adjustment) % 7

    print(f"{year}-{month}-{day} is a {dotw_index[result]}")

def dateoverflow(month, day, year):
    overflow = day_overflow[month - 1]

    if month == 2:
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            overflow = 29

    if day > overflow:
        day -= overflow
        month += 1

    return month, day

def makeCalendar(year, offset):
    month = 1
    day = 1

    while month <= 12:
        getDayOfTheWeek(year, month, day, offset)

        day += 1
        month, day = dateoverflow(month, day, year)
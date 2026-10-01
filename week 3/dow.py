month_index = [1, 4, 4, 0, 2, 5, 0, 3, 6, 1, 4, 6]
monthDict = {"January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6, "July": 7, "August": 8, "September": 9, "October": 10, "November": 11, "December": 12}
dotw_index = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
offset_index = [6, 4, 2, 0, 6, 4]
day_overflow = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def getoffset(year):
    offset = (year % 1600) // 100
    return offset

def getDayOfTheWeek(year, month, day, offset): #day of the week calculation
    decade = year % 100

    step1 = decade // 12
    step2 = decade % 12
    step3 = step2 // 4
    step5 = month_index[month - 1]

    leap_adjustment = 0

    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0): #leap year checker and adjustment
        if month <= 2:
            leap_adjustment = -1

    result = (step1 + step2 + step3 + day + step5
              + offset_index[offset] + leap_adjustment) % 7

    print(f" \n{year}-{month}-{day} is a {dotw_index[result]}\n ")

def dateoverflow(month, day, year): #converting to date format

    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0): #leap year adjustment for date format
            day_overflow[1] = 29

    if day > day_overflow[month - 1]:
        day -= day_overflow[month - 1]
        month += 1

    day_overflow[1] = 28
    return month, day

def makeCalendar(year, offset): #loop from the start to the end of the year
    month = 1
    day = 1

    while month <= 12:
        getDayOfTheWeek(year, month, day, offset)

        day += 1
        month, day = dateoverflow(month, day, year)
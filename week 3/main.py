import dow

def getDayOfTheWeekForUserDate():
    year = int(input("Year: "))
    month = int(input("Month: "))
    day = int(input("Day: "))

    offset = dow.getoffset(year)

    dow.getDayOfTheWeek(year, month, day, offset)

year = int(input("Input year for every day of the year: "))
offset = dow.getoffset(year)

dow.makeCalendar(year, offset)

getDayOfTheWeekForUserDate()
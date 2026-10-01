import dow

def getDayOfTheWeekForUserDate():
    year = int(input("Year: "))
    month = int(input("Month: "))
    day = int(input("Day: "))

    offset = dow.getoffset(year)

    dow.getDayOfTheWeek(year, month, day, offset)

def program():
    decision = 0

    while decision != 3:
        print("(1) Get day of the week for a specific date")
        print("(2) Get day of the week for an entire year")
        print("(3) Exit")

        decision = int(input("Input: "))

        if decision == 1:
            getDayOfTheWeekForUserDate()

        if decision == 2:
            year = int(input("Input year for every day of the year: "))
            offset = dow.getoffset(year)

            dow.makeCalendar(year, offset)

program()
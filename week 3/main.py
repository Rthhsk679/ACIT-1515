import dow

def getDayOfTheWeekForUserDate():
    year = int(input("Year: "))

    monthinput = (input("Month: ").capitalize())
    if monthinput.isnumeric():
        month = int(monthinput)
    else:
        month = dow.monthDict[monthinput]

    day = int(input("Day: "))

    offset = dow.getoffset(year)

    dow.getDayOfTheWeek(year, month, day, offset)

def program(): #simple interface
    decision = 0

    while decision != 3:
        print("(1) Get day of the week for a specific date\n(2) Get day of the week for an entire year\n(3) Exit\n\nNote: month works with both string and int!")

        decision = int(input("Input: "))

        if decision == 1:
            getDayOfTheWeekForUserDate()

        if decision == 2:
            year = int(input("Input year for every day of the year: "))
            offset = dow.getoffset(year)

            dow.makeCalendar(year, offset)

program()
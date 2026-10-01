import dow

def getDayOfTheWeekForUserDate():
    year = int(input("Year: "))

    monthinput = (input("Month: ").capitalize()) #To let inputed month be either string or int
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
        decision = int(input(" \n(1) Get day of the week for a specific date\n(2) Get day of the week for an entire year\n(3) Exit\n\nInput: "))

        if decision == 1:
            getDayOfTheWeekForUserDate()
            input("Continue...")

        if decision == 2:
            year = int(input("Input year for every day of the year: "))
            offset = dow.getoffset(year)

            dow.makeCalendar(year, offset)
            input("Continue...")

        elif decision > 3:
            input("Invalid input...")

program()
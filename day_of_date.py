import calendar
def getcalendar():
    year = int(input("Enter the year: "))
    print(calendar.calendar(year))

    months_with_5_sundays = [ ]
    for month in range(1,13):
        #days_in_month = calendar.monthcalendar(year,month)
        #print(f"List of the week with 5dayas: {days_in_month}")
        for week in calendar.monthcalendar(year,month):
            # if week[calendar.SUNDAY] !=0: # Sunday = 0 in calendar
            #     print(f"{calendar.month_abbr[month]} {week[calendar.SUNDAY]}")
            for day in week:
                if day!=0 and calendar.weekday(year,month,day) == calendar.SUNDAY:
                    name_of_day = calendar.day_abbr[calendar.weekday(year, month, day)]
                    # print(f"{calendar.month_abbr[month]} {day}, {name_of_day}")

                    if day >= 29:
                        print(f"The 5th Sunday of the year: {calendar.month_abbr[month]} {day}, {name_of_day}")

calender = getcalendar()
print(calender)

#to test the git branch



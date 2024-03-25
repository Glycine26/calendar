'''I need to get the dates of the 5th Sundays of any year'''


import calendar
def getcalendar():
    year = int(input("Enter the year: "))
    print(calendar.calendar(year))

    for month in range(1,13):
        for week in calendar.monthcalendar(year,month):
            for day in week:
                if day!=0 and calendar.weekday(year,month,day) == calendar.SUNDAY and day >= 29:
                    name_of_day = calendar.day_abbr[calendar.weekday(year, month, day)]
                    print(f"The 5th Sunday of the year: {calendar.month_abbr[month]} {day}, {name_of_day}")

calender = getcalendar()
print(calender)

'''day!=0 is used to filter out days that are not part of the current month.
-In the matrix returned by calendar.monthcalendar, each element corresponds to a day of the month.
-Days outside the current month (i.e., days before the 1st or after the last day of the month) are represented by 0.
-To ensure the days are only part of the current month'''
"To push back"
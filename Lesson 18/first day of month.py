import calendar

#first day of month
c = calendar.TextCalendar(calendar.SUNDAY)

str = c.formatmonth(2024,9)
print("calendar for the month is")
print(str)
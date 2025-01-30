def day_0f_year(date):
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    #here it splits up the date in year,month,day
    year, month, day = map(int, date.split('-'))
    #checking if for leap year or not
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        days_in_month[1] = 29  
    
    days=0
    for i in range(month - 1):
        days += days_in_month[i]
    return days + day

date = input("Enter date (YYYY-MM-DD): ")
output1 = day_0f_year(date)

print("Date:" ,date, ", Day of Year:" ,output1)
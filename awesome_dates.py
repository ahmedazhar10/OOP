import datetime
from dateutil.relativedelta import relativedelta

now = datetime.date(2018, 5, 18)
#print(now.year)
#print(now.month)
#print(now.day)
#print(datetime.date.today()) #Prints today's date

#calculating ages

today = datetime.date.today()
birthday = datetime.date(1998, 6, 13)
rdelta = relativedelta(now, birthday)

age = today - birthday
print(age)

print("Age in years = ", rdelta.years)
#print("Age in months = ", rdelta.months)
#print("Age in days = ", rdelta.days)
#next_day = datetime.timedelta(days=1)
#today += next_day
#print(today)

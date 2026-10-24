city= input("Enter your city name: ")
temp= float(input("Enter your city's temperature in C: "))
if temp > 35 :
    print("HOT!!")
if temp > 35:
    print("HOT!!!")
else :
    print("Ok")
if temp  > 35:
    print("VERY HOT!")
elif temp > 25 :
    print("Nice and warm")
elif temp > 15:
    print("Cold")
else :
    print("STAY INSIDE!!")
import datetime
now= datetime.datetime.now()
print("Current date/time now ", datetime.datetime.now())
import calendar
print("Current year ", calendar.calendar(now.year))
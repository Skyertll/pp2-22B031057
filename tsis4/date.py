#1
from datetime import *

current_date = date.today()
new_date = current_date - timedelta(days=5)

print("Today:", current_date)
print("Five days ago:", new_date)

#2
today = date.today()

yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print("Yesterday:", yesterday)
print("Today:", today)
print("Tomorrow:", tomorrow)

#3
current_datetime = datetime.now()
new_datetime = current_datetime.replace(microsecond=0)

print(current_datetime)

#4
date1 = datetime.now()
date2 = datetime(2023, 1, 1, 5, 30, 0)

difference = (date2 - date1).total_seconds()

print("The difference between", date1, "and", date2, "is", difference, "seconds.")


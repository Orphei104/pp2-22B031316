import datetime

current_date = datetime.datetime.now()
new_datetime = current_date.replace(microsecond=0)

print("Current datetime:", current_date)
print("New datetime:", new_datetime)

import datetime

current_date = datetime.date.today()
new_date = current_date - datetime.timedelta(days=5)

print("Current date:", current_date)
print("New date:", new_date)
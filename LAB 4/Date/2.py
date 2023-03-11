import datetime

current_date = datetime.date.today()
yesterday = current_date - datetime.timedelta(days=1)
tomorrow = current_date + datetime.timedelta(days=1)

print("Yesterday:", yesterday)
print("Today:", current_date)
print("Tomorrow:", tomorrow)
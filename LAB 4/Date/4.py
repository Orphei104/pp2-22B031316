import datetime

date1 = datetime.datetime.today()
date2 = date1 - datetime.timedelta(seconds=90)

a = date1 - date2
difference = a.total_seconds()

print(f"Difference between date2 and date1 in seconds: {a}")

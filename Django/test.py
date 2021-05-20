import datetime

date = datetime.date(2077, 3, 14)
today = datetime.date.today()
print(abs((today - date).days))
print(date.year)
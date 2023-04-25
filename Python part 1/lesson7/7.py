#import datetime
from datetime import date, time, datetime

#now = datetime.datetime.now()
#print(now)

#now1 = datetime.date.today()
#print(now1)

#d = datetime.date(2023, 3, 21)
#print(d.year)
#print(d.month)
#print(d.day)

a = time()
print(a)


b = time(11,34,56)
print(b)

print(b.hour)
print(b.second)

c = datetime(2023, 3, 21)
print(c)

print(c.timestamp())
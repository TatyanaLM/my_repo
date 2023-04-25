from datetime import date, time, datetime, timedelta

#t1 = date(2018, 7, 12)
#t2 = date(2017, 12, 23)

#t3 = t1 - t2

#print(t3)

t1 = timedelta(weeks=2, days=3, hours=1, seconds=55)
t2 = timedelta(days=4, hours=11, minutes=4, seconds=5)

t3 = t1 - t2
print("t3 = ", t3)
print(t3.total_seconds())

now = datetime.now()
t = now.strftime("%H:%M:%S")
print(t)

s1 = now.strftime("%m/%d/%Y, %H:%M:%S")
print(s1)
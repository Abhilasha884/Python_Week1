'''Creating a date object'''
from datetime import datetime,date,time
d=date(2002,6,3)
print(d)

'''Get current date'''

t=date.today()
print(t)

'''Convert date from timestamp'''

date_time=datetime.fromtimestamp(1887639468)
print(date_time)
'''to get hr minute second and microsecond'''
Time = time(11, 34, 56)
print("hour =", Time.hour)
print("minute =", Time.minute)
print("second =", Time.second)
print("microsecond =", Time.microsecond)

'''to convert to string'''
str=time.isoformat()
print(str)

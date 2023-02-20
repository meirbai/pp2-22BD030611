import datetime
from datetime import timedelta

x = datetime.datetime.now()
y = x - timedelta(days=1)
z = x + timedelta(days=1)
print("Yesterday:" , y)
print("Today:" , x)
print("Tomorrow:" , z)
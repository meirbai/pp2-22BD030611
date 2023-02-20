import datetime
from datetime import timedelta

x = datetime.datetime.now()
x1 = x - timedelta(days=5)
print(x1)
import datetime as dt
from datetime import timedelta

x = dt.datetime.now()
y = dt.datetime.now() + timedelta(days=1)
c = str((y-x).total_seconds())
f = slice(len(c)-7)
print(c[f])
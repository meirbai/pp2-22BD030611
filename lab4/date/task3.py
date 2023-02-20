import datetime
from datetime import timedelta

x = datetime.datetime.now()
x1 = str(x)
y = slice(len(x1)-7)
print(x1[y])
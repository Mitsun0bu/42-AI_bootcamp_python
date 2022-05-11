kata = (2019, 9, 25, 3, 30)

import datetime as dt

date = dt.date(year=kata[0], month=kata[1], day=kata[2])
date_str = date.strftime("%m/%d/%Y ")
hour = dt.time(hour=kata[3], minute=kata[4])
hour_str = hour.strftime("%H:%M")
final_str = date_str + hour_str
print(final_str)
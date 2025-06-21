import datetime as dt

# Soal no 1

dateCostum = dt.datetime(2021, 6, 12, 15, 35, 10)

print(dateCostum.strftime("%d %B %Y %H:%M"))

print(dateCostum.strftime("%Y/%m/%d %I:%M %p"))

print(dateCostum.strftime("Jam %I Lewat %M Menit"))
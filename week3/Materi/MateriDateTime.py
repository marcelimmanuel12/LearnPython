import datetime as dt
from dateutil.relativedelta import relativedelta

# creat date now
dateNow = dt.datetime.now()
print(f"Date time now = {dateNow}")

# crate date costume
dateCostum = dt.datetime(2021, 3, 28, 17, 10, 2)
print(f"Date costum = {dateCostum}")
# susunan isi parameter di atas
# tahun, bulan, tanggal, jam, menit, detik

dateCostum = dt.datetime(2022, 11, 8)
print(f"Date costume = {dateCostum}")

# Manipulasi kondisi date dan time
# contoh:
# (1) tambahan 5 bulan ke depan dari variable dateCostum 
# (2) kurangi 1250 detik dari variable dataeCostume ( nyambung dari kondisi 1)
# (3) tambah 75 menit dari dateCostum (nyambung dari kodisi)

dateCostum = dateCostum +relativedelta(months=5)
print(f"Setelan tambahan 5 bulan menjadi = {dateCostum}")

dateCostum = dateCostum + relativedelta(seconds=-1250)
# dateCostum = dateCostum - relativedelta(seconds=1250) 3 #Cara kedua(sama ajh)
print(f"\nSetelah kurangi 1250 detik menjadi = {dateCostum}")

dateCostum = dateCostum + relativedelta(minutes=75)
print(f"\nSetelah tambah 75 menit menjadi = {dateCostum}")

# formatting date
# pembuatan patten terdahap format data
# memanfaatkan format simbol simbol

# contoh 
print(dateCostum.strftime("%d %B %Y %H:%M:%S"))

#w3schools python datetime
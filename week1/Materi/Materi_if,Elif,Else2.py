# contoh if , elif , else

nilai1 = float(input("Maukan nilai 1 :"))
nilai2 = float(input("Maukan nilai 2 :"))
nilai3 = float(input("Maukan nilai 3 :"))
nilai4 = float(input("Maukan nilai 4 :"))

nilai_rata2 = (nilai1 +nilai2 + nilai3 + nilai4) / 4
nilai_min = 58

keterangan = "" #string kosong
if (nilai_rata2 >= 90):
    if(nilai_rata2 < 94 or nilai_rata2 > 98):
        keterangan = "Perfect"
    else:
        keterangan = "Mantap"

elif (nilai_rata2 >= 80):
    if (nilai_rata2 > 82 and nilai_rata2 != 85 and nilai_rata2 < 88) :
        keterangan = "Oke"
    else:
        keterangan = "Sip"

elif (nilai_rata2 >= nilai_min):
    if (nilai_rata2 > 75) :
        keterangan = "Baik"

    elif (nilai_rata2 >= 65) :
        keterangan = "Standar"

    else:
        keterangan = "Cukup"

else:
    keterangan = "Tidak lulus"


text_output = f"""Nilai rata-rata = {nilai_rata2}
keterangan = {keterangan}"""

print(text_output)
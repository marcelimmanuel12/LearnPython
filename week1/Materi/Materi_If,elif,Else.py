input_angka = input("masukan sebuah angka : ")
print(f"Angka yang anda input adalah {input_angka}")

input_angka = float(input_angka)

# condotional programming menggunakan if , else
if input_angka >= 60:  
    print("Anda lulus")
else:
    print("Maaf, Anda tidak lulus")


print(f"n\n\n")

# conditional programming menggunakan match case
nama_bulan = input("Masukan sebuah nama  bulan dalam penanggalan :")
nama_bulan = nama_bulan.upper() # function upper --> membuat teks dalam string jadi huruf besar semua

teks_bulan = ""

match (nama_bulan):
    case "JANUARI":
        teks_bulan = "1"

    case "FEBRUARI":
        teks_bulan = "2"

    case "MARET":
        teks_bulan = "3"

    case "APRIL":
        teks_bulan = "4"

    case "MEI":
        teks_bulan = "5"

    case _:
        teks_bulan = "Maaf angka belum tersedia"


print (f"""Nama_bulan = {nama_bulan}
Angka bulan = {teks_bulan}""")
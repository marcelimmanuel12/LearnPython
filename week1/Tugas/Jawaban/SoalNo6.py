# Latihan soal no 6

print("=== Program biaya penyewaan mobil ===")

kelasmobil = input("""Pilih tipe pembayaran
                   (A) Sedan --> Harga sewa Rp 350.000 / hari
                   (H) Hatchback --> Harga sewa Rp 600.000 / hari
                   (M) MPV --> Harga sewa Rp 320.000 / hari
                   (S) Sport --> Harga sewa Rp 600.000 / hari
                   (T) Truck --> Harga sewa Rp 750.000 / hari : """)

kelasmobil = kelasmobil.upper()

if(kelasmobil == "A"):
    A = 350000

elif(kelasmobil == "H"):
    A = 600000

elif(kelasmobil == "M"):
    A = 320000

elif(kelasmobil == "S"):
    A = 600000

elif(kelasmobil == "T"):
    A = 750000

lamaharisewa = int(input("Masukan berapa hari sewa mobil :"))

if (lamaharisewa >= 1) and (lamaharisewa<7):
    B = A*0
    print ("Kamu tidak mendapat diskon =", int(B))
elif (lamaharisewa >= 8) and (lamaharisewa <30):
    B = A*(5/100)
    print ("Kamu mendapatkan diskon 5 persen =", int(B))
elif(lamaharisewa >= 31) and (lamaharisewa <60):
    B = A*(10/100)
    print ("Kamu mendapatkan diskon 10 persen =", int(B))
elif(lamaharisewa <60):
    B = 0
    print ("Kamu tidak diizinkan", int(B))

C = A-B

teks_output = f"""Jumlah yang harus dibayarkan = (Rp){C}"""

print(teks_output)
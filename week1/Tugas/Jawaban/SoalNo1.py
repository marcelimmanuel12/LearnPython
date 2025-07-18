import math

print("=== Program simulasi pembelian apartemen ===")

hargaApartemen = int(input("Masukan harga apartemen (Rp) :"))
metodePembayaran = input("""Pilih tipe pembayarean 
                         (A) Pembayaran tunai (diskon 10%)
                         (B) Pembayaran betahap (cicil 12x diskon 5%)
                         (C) Pembayaran kredit (cicil 50x) : """)

metodePembayaran = metodePembayaran.upper()

totalBayar = 0
cicilan = 0
keterangan = ""

if (metodePembayaran == "A"):
    # tunai dan diskon 10%, tidak ada cicilan
    totalBayar = (90/100) * hargaApartemen
    keterangan = "Pembayaran tunai, diskon10%"

elif (metodePembayaran == "B"):
    # Bertahap,diskon 5%, cicil 12x
    totalBayar = math.ceil( (95/100) * hargaApartemen)
    cicilan = math.ceil( totalBayar/ 12 )
    keterangan = "Pembayaran bertahap, diskon 5%, cicil 12x"

elif (metodePembayaran == "C"):
    # kredit, tidak ada diskon, cicil 50x
    totalBayar = hargaApartemen
    ciciclan = math.ceil( totalBayar / 50 )
    keterangan = "Pembayaran kredit, cicil 50x"

else:
    # kondisi salah input kode metode pembayaran
    keterangan = "Salah input kode metode pembayaran, Silahkan periksa kembali"

textOutput = f"""Total bayar (RP) = {totalBayar}
Cicilan (Rp) = {cicilan}
Keterangan = {keterangan}"""

print(textOutput)
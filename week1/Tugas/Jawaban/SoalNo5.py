# Latihan soal no 5

print("=== Program simulasi pembayarn air ===")

jumlahpemakaian = int(input("Masukan jumlah pemakaian :"))

Tagihan = ""

if(jumlahpemakaian < 100):
    if(jumlahpemakaian >0 and jumlahpemakaian <100):
        Tagihan = "Rp.200.000,-"

elif(jumlahpemakaian < 300):
    if(jumlahpemakaian >100 and jumlahpemakaian <300):
        Tagihan = 200.000 + (jumlahpemakaian - 100) *2500

elif(jumlahpemakaian > 900):
    Tagihan = 900.000 + (jumlahpemakaian - 900) *3.000

else:
    Tagihan = "Salah input kode metode pembayaran, Silahkan periksa kembali"

text_output = f"""Total biaya pemakaian air yang harus dibayarkan = {Tagihan}"""

print(text_output)
# Latihan soal no 3

print("=== Program mengitung biaya ansuransi ladang ===")

jenisladang = input("""Pilih jenis ladang
                    (A) Pertanian standar = 3.5%
                    (B) Ladang kacang kedelai,kentang,bawang merah,cabai = 2%
                    (C) Ladang padi dan jagung = 1.5% :""")

hargatanah = int(input("Masukan harga tanah (Rp) :"))

luastanah = int(input("Masukan luas tanah :"))

if(jenisladang == "A"):
    A = 3.5/100

elif(jenisladang == "B"):
    A = 2/100

elif(jenisladang == "C"):
    A = 1.5/100

biayaansuransi = A*hargatanah*luastanah

text_output = f"""Jumlah yang harus dibayarkan = (Rp){biayaansuransi}"""

print(text_output)
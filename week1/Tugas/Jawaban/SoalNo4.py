#Latihan soal no 4

print("=== Program untuk mengkategorikan niai indeks polusi ===")

nilaiindekspolusi = int(input("Masukan nilai indeks polusi :"))

keterangan = ""
if (nilaiindekspolusi < 35):
        keterangan = "Nyaman"
elif (nilaiindekspolusi < 60):
        if (nilaiindekspolusi > 35 and nilaiindekspolusi < 60):
               keterangan = "Tidak nyaman"
elif (nilaiindekspolusi > 60):
        keterangan = "Berbahaya"

text_output = f"""nilai indeks polusi = {nilaiindekspolusi}
keterangan = {keterangan}"""

print(text_output)
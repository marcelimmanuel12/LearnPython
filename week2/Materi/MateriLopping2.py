# looping for untuk data list

listKota = ["Banda Aceh", "Denpasar", "Pangkal pinang", "Cilegon", "Serang", "Tanggerang selatan", "Bengkulu"]

#               0               1              2            3          4               5                 6

for kota in listKota:
    print(kota)
    print("============")

print(f"\n\n")

# bisa juga menggunakan for versi range untuk looping data list
# memanfaatkan angka index dari list
for i in range(0, len(listKota), 1):
    print(f"Nama kota ke {i+1} dalam list adalah {listKota[i]}") # get data by index position
    print("===========")
print(f"/n/n")

# ada 2 perintah dalam looping
# (1) continue
# (2) break

# continue adalah perintah dalam looping untuk memakasa supaya loopig lanjut ke interasi berikutnya
# contoh: jika nama kota == "Cilegon" atau "Denpasar", maka continue

for kota in listKota:
    if (kota == "Cilegon"  or kota == "Denpasar"):
        continue
    
    print(kota)
    print("======")


print(f"\n\n")


# break adalah perintah dalam looping untuk memaksa looping berhenti
# contoh: jika nama kota == "Serang" maka break

for kota in listKota:
    if (kota == "Serang"):
        break

    print(kota)
    print("=======")
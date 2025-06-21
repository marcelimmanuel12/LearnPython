namaKota = ["Banda Aceh", "Medan", "Bengkulu", "Riau", "Pangkal pinang"]
kumpulanAngka = [56, 12, 3, 25, 17.5, 5.5, 10, 8, 45.6, 6]
dataCampuran = [60.125, True, "Jeruk", 75, ["jerapah", "Kucing"]]

jumlahNamaKota = len(namaKota)
jumlahDataAngka = len(kumpulanAngka)
jumlahdatacampuran = len(dataCampuran)

print(f"{namaKota}")
print(f"{kumpulanAngka}")
print(f"{dataCampuran}")

print(f"\n\n")
print(f"Jumlah nama kota = {jumlahNamaKota}")
print(f"Jumlah data angka = {jumlahDataAngka}")
print(f"Jumlah data campuran= {jumlahdatacampuran}")

namaKotaIndex3 = namaKota[3] # get
#namaKotaIndex6 = namaKota[6] # dicomment karena error list inex of range
angkaIndex5 = kumpulanAngka[5]

print(f"\n\n")
print(f"Nama kota index 3 adalah {namaKotaIndex3}")
#print(f"Nama kota index 6 adalah {namaKotaIndex6}")
print(f"Angka posisi index ke 5 adalah {angkaIndex5}")


# change value ==> set
namaKota[3] = "Palembang" # set (mengganti riau mejadi palembang)
print(f"{namaKota}")


# get data by index
namaKotaIndex1_4 = namaKota[1:5] # 1 : 5 artinya dari index 1 sampai 4
namaKotaIndex1_Last = namaKota[1:] # 1 : artinya dari index 1 sampai index terakhir
namaKotaIndex0_3 = namaKota[:4] # : 4 artinya dari index 0 sampai 3

print(f"\n\n")
print(f"Nama kota index 1 sampai 4 = {namaKotaIndex1_4}")
print(f"Nama kota index 1 sampai terakhir = {namaKotaIndex1_Last}")
print(f"Nama kota index 0 sampai 3 = {namaKotaIndex0_3}")


# function append ==> function untuk  menambahkan data baru dalam list
# ke posisi index paling akhir (create new index)

namaKota.append("Jakarta")
print(f"n\n")
print(f"setelah append 1 kota baru menjadi = {namaKota}")

# function insert ==> function untuk menambahkan data baru ke dalam list,
# ke posisi index spesifik yang dimasukkan ke parameter insertnya
# misal : insert di index ke 3,kota "Surabaya"
namaKota.insert(3, "Surabaya")
print(f"\n\n")
print(f"Setelah insert 1 kota baru menjadi = {namaKota}")

# function extend ==> function untuk menggabungan 2 varible list menjadi 1 
# misal: extend list namaKota dengan kumpulanAngka 
namakota2 = ("Samarinda", "Solo", "Bnajarmasin")
namaKota.extend(namakota2)
print(f"\n\n")
print(f"Setelah extend menjadi = {namaKota}")

# function remove ==> function untuk menghapus data dalam list berdasarkan value nya 
# misal: remove kota dengan value = "Jakarta" dan "Denpasar"
namaKota.remove("Jakarta")
if ("Denpasar" in namaKota or "denpasar" in namaKota):
    namaKota.remove("Denpasar")
print(f"\n\n")
print(f"Setelah remove menjadi = {namaKota}")

# function pop ==> function untuk menghapus data dalam list berdasarkan posisi index 
# misalnya mau menghapus data posisi paling akhir
jumlah = len(namaKota)
namaKota.pop(jumlah - 1)
print(f"\n\n")
print(f"Setelah pop menjadi = {namaKota}")

# function sort ==> function untuk mengurutkan dari data dalam list
# jika data srting maka sorting berdasarkan urutan alfabet
# jika data number makna sorting berdasarkan nilai angka itu sendiri

# sort ascending (sorting yang arahnya dari kecil ke besar)
namaKota.sort()
print(f"\n\n")
print(f"Setelah sort ascending menjadi = {namaKota}")

kumpulanAngka.sort()
print(f"\n\n")
print(f"Angka setelah sort ascending menjadi = {kumpulanAngka}")

# sort ascending (sorting yang arahnya dari besar ke kecil)
namaKota.sort(reverse=True)
print(f"\n\n")
print(f"Setelah sort ascending menjadi = {namaKota}")

kumpulanAngka.sort(reverse=True)
print(f"\n\n")
print(f"Angka setelah sort ascending menjadi = {kumpulanAngka}")

# Function clear ==> function untuk menghapus semua data yang ada didalam list
# sehingga menjadi list kosong 
namaKota.clear()
kumpulanAngka.clear()

print(f"\n\n")
print(f"Setelah clear nama kota menjadi = {namaKota}")
print(f"Angka setelah clear mejadi = {kumpulanAngka}")
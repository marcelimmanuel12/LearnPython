import math
import random

# ini contoh comment

# contoh multiline comment
# test 123
# test 321

namaSiswa = "Anto Susanto"
nilaiSiswa = 80.5
nilaiSiswa += 3

print ("Nama siswa adalah " + namaSiswa + " Nilai = " + str(nilaiSiswa))

print(f"Nama siswa adalah {namaSiswa} Nilai = {str(nilaiSiswa)}")
# teknik string interpolation --> menyisipkan variabel dalam String
#menggunakan {}

nilaiSiswaInt = int(nilaiSiswa)
print(f"Nilai integer = {nilaiSiswaInt}")


lulus = True # assign
print(f"Lulus = {lulus}")

lulus = not lulus # re-assign
print(f"lulus = {lulus}")

# contoh tipe data lst
namaHewan = [ "Gajah", "Kucing", "Kura Kura", "Ikan" ]
kumpulanAngka = [20.125, 15, 32.56, 25, 19.28]
kumpulanDataCampuran = [ True, "Belajar programming", 56, 12.5, {"Test 1", "Test 2"} ]

# contoh tipe data dictonary (key, value)
dataKaryawan = { "nama" : "Budi Setiawan",
                "alamat" : "Jl. Mangga No 12",
                "Berkeluarga" : False,
                "hobby" : ["Mancing", "Membaca buku"] }

# get value from dictionary by key
dataHobby = dataKaryawan["hobby"]
dataAlamat = dataKaryawan["alamat"]

print(str(dataKaryawan))
print(f"Hobby = {dataHobby}")
print(f"Alamat = {dataAlamat}")

print(f"n\n\n")

result = math.pow(8, 2)
print(f"result 1 = {result}")
result -= 5
print(f"Result 2 = {result}")
result *= 2
print(f"Result 3 = {result}")
result /= 2
print(f"result 4 = {result}")

result = math.ceil(result)
print(f"Hasil ceil = {result}")

print(f"n\n\n")

randomNumber = random.randint(1, 1000)
print(f"Angka random yang didapat = {randomNumber}")
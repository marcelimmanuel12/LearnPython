import datetime as dt

dataSiswa = {
    "Nama" : "Supriyanto Gunawan", 
    "Alamat" : "Jl. Mangga 2 No.30 RT 009 RW 007", 
    "Hobby" : ["Membaca buku,", "Futsal", "Berenang", "Sepedaan"],
    "Nama Ayah" : "Tono",
    "Nama Ibu" : "Tini",
    "Usia" : 12,
    "Kakak" : False, 
    "Adik" : True,
    "Tanggal lahir" : dt.datetime(day=10, month=9, year=2024)
}

# Len ==> menghitung jumlah key, value yang ada dalam Dictionary
jumlahData = len(dataSiswa)
print(f"{dataSiswa}")

print(f"\nJumlah data dictionary = {jumlahData}")

# get data by key
alamatSiswa = dataSiswa["Alamat"]
alamatSiswaV2 = dataSiswa.get("Alamat")

# Jika key tidak ditemukan, maka bisa berikan default value
tempatLahirSiswa = dataSiswa.get("Tempat Lahir", "Data tidak tersedia")


print(f"Alamat Siswa = {alamatSiswa}")
print(f"Alamat siswa v2 = {alamatSiswaV2}")
print(f"Tempat lahir siswa = {tempatLahirSiswa}")


dataSiswa["Nama Ibu"] = "Ibu Susi"
dataSiswa["Nama Ayah"] = "Bapak Gunardi"
dataSiswa["Tempat Lahir"] = "Jakarta"

print(f"\n\n{dataSiswa}")

# Function pop ==> untuk  menghapus data di dalam Dictonary
# Berdasarkan key

if "Hobby" in dataSiswa:
    dataSiswa.pop("Hobby")

if "Nama Adik" in dataSiswa:
    dataSiswa.pop("Nama Adik")

print(f"\n\n{dataSiswa}")


# function popitem ==> function untuk menghapus data yang posisi key,value paling belakang
dataSiswa.popitem()
print(f"\n\n{dataSiswa}")


# function clear ==> function untuk menghapus semua data di dalam Dictonary
# sehingga menjadi Dictonary kosong
dataSiswa.clear()
print(f"\n\nSetelah diclear menjadi {dataSiswa}")
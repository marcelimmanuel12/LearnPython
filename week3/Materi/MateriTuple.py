namaKota = ["Banda Aceh", "Medan", "Bengkulu", "Riau", "Pangkal pinang"]

# Tuple bisa get data by index 
namaKotaIndex3 = namaKota[3]

# Tuple bisa untuk di hitung  length nya
jumlahKota = len(namaKota)

print(f"{namaKota}")
print(f"Nama kota index ke 3 = {namaKotaIndex3}")

print(f"Jumlah kota = {jumlahKota}")


# namaKota[3]  # tuple tidak bisa dilakukan re-assign value
# print(f"\n{namaKota}")


namaKotaList = list(namaKota)
namaKotaList.append("Jayapura")
namaKotaList.append("Lombok")
namaKota = tuple(namaKotaList)

print(f"{namaKota}")
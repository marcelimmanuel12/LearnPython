# Latihan soaL NO 4
from MyModule import MyClass

print ("=== Program function menghitung luas trapesium ===")
# Rumus versi pertemuan 1
sisi_1 = int(input("Masukan sisi 1 : "))
sisi_2 = int(input("Masukan sisi 2 : "))
tinggi = int(input("Masukan tinggi : "))

luas = 1 / 2 * (sisi_1 + sisi_2) * tinggi
print ("Luas Trapesium : ", luas)

print(f"\n\n")

# Rumus function versi diri sendiri
s = int(input("Masukan sisi 1 : "))
s = int(input("Masukan sisi 2 : "))
t = int(input("Masukan tinggi : "))

mc = MyClass
LS = mc.hitungluastrapesium(s, t)
print(f"Luas trapesium12 adalah {LS}")
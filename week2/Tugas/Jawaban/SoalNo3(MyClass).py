# Latihan soal no 3

from MyModule import MyClass

print("=== Program function chek huruf===")

nilai = int(input("Masukan grade anda :"))

mc = MyClass()
keterangan = mc.chekhuruf(nilai)
print(f"Grade = {keterangan}")
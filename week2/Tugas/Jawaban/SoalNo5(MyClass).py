# Latihn soal no 5
from MyModule import MyClass

penghasilan = int(input("Masukan penghasilan :"))
mc = MyClass
pajak = mc.hitung_pajak(penghasilan)
print(f"Pajak yang harus dibayarkan : Rp {pajak}")
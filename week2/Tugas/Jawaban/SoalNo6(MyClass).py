# Latihan soal no 6
from MyModule import MyClass
    
a = int(input("Masukan angka 1 :"))
b = int(input("Masukan angka 2 :"))

print (f"{a}*{b}= ", end="")
print (" + ".join([str(a)] * b), end=" ")
print (f"hasilnya {a*b}")
#Latihan soal no 2

#Kalkulator sederhana
print(20*"=")
print("Kalkurator Sederhana")
print(20*"=" + "\n")

angka_1 = float(input("Masukan angka 1 = "))
operator = input("operator (+,-,x,/) : ")
angka_2 = float(input("Masukan angka 2 = "))

# Percabangannya

if operator == "+": 
    hasil = angka_1 + angka_2
    print(f"hasilnya adalah {hasil}")
elif operator == "-":
    hasil = angka_1 - angka_2
    print(f"hasilnya adalah {hasil}")
elif operator == "x":
    hasil = angka_1 * angka_2
    print(f"hasilnya adalah {hasil}")
elif operator == "/":
    hasil = angka_1 / angka_2
    print(f"hasilnya adalah {hasil}")

print("Akhir dari program, terima kasih ")
# looping dibedakan menjadi 2:
# (1) looping increment --> looping yang aman iterasinya naik (dari kecil ke besar)
# (2) looping decrement --> looping yang arah iterasinya turun (dari besar ke kecil)

# studi kasus : anak ayam ---> anak ayam bisa mati dan bisa lahir

jumlahAnakAyam = int(input("Masukan jumlah anak ayam : "))

# contoh looping for incrument
for i in range(0, jumlahAnakAyam, 1):
    print(f"Anak ayam semula {i}, lahir 1 menjadi {1+1}")
    print("=============================================")

print(f"\n\n")

# contoh looping for decrement
for i in range(jumlahAnakAyam, 0,-2):
    # setiap looping, nilai i berkurang 2
    if (i-2 >= 0): # untuk angka ganjil 
        print(f"Anak ayam awalnya ada {i}, mati 2 tersisa {i-2}")
        print("==============================================")


print(f"n\n")

# contoh looping while increment
j = 0
while (j < jumlahAnakAyam):
    print(f"Anak ayam awalnya {j}, lahir 3 menjadi {j+3}")
    print("===============================================")
    j += 3

print(f"n\n")

# contoh looping while decrement
j = jumlahAnakAyam
while (j > 0):
    if (j-3 >=0):
        print(f"Anak ayam mula-mula {j}, mati 3 maka tersisa {j-3}")
        print("==============================================")

    j -= 3
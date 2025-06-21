# try catch atau di python dinamakan try except
# merupakan perintah untuk melakukan error handling

import random

print("=== Belajar error handling ===")
print("=== Menggunakan try except ===")

try:
    inputAngka = float(input("Masukan sebuah angka : "))
    angkaRandom = random.radiant(1, 100)
    result = inputAngka * angkaRandom

    print(f"Angka random = {angkaRandom}\nResult = {result}")

except:
    print("Terjadi error, mohon input angka dengan benar")

print("== Program end ==")


# contoh try except untuk melakukan  validasi
# tugas pertemuan 7 no 2

# raise adalah perintah agar eksekusi code terlempar ke except

try:
    inputan = input("Masukan sebuah angka ganjl diantar 50 s/d 100 : ")

    # validasi 
    if (inputan ==""):
        raise Exception("Inputan angka kosong !!")
    
    if(not inputan.isnumeric()):
        raise Exception("Inputan harus angka yang valid !!")
    
    inputanAngka = int(inputan)
    if(inputanAngka %2 == 0):
        raise Exception("Angka yang di input harus bilangan ganjil")
    
    if(inputanAngka < 50 or inputanAngka > 100):
        raise Exception("inputan angka tidak boleh < 50 dan tidak boleh > 100")

    # kondisi lolos validasi
    print(f"Success\nAngka ganji yang anda input = {inputanAngka}")

except Exception as ex:
    print(f"failed\nPesan error : {str(ex)}")
import random
import math

# Contoh function yang tidak memiliki palameter dan tidak meengemmbalikan hasil
def createRandomNumber() -> None:
    randomNo1 = random.randint(1, 100)
    print(f"Randomm number 1 = {randomNo1}")

    randomNo2 = random.randint(1, 1000)
    print(f"Random number 2 = {randomNo2}")

# None / void adalah istilah function yang tidak mengembalikan hasil

createRandomNumber()


# contoh function yang memiliki 2 parameter dan tidak mengembalikan hasil 
def hitungVolumeTabung(r: float, t: float) -> None:
    volume = (22/7) * (r ** 2) * t # cara 1
    #volume2 = math.pi * math.pow(r, 2) * t , cara 2
    print(f"Volume tabung (1) = {volume}") # Cara 1
    #print(f"Volume tabung (2) = {volume2}") , cara 2


jariJari = float(input("Masukkan jari jari tabung (cm) : "))
tinggi = float(input("Masukkan tinggi tabung (cm) : "))
hitungVolumeTabung(jariJari, tinggi)


# Contoh function yang memiliki 2 parameter dan mengembalikan hasil dengan tipe float
def hitungVollumeTabungV2(r: float, t: float) -> float:
    volume = (22/7) * (r** 2) * t
    return volume

volumeAkhir = hitungVollumeTabungV2(jariJari, tinggi)
print(f"Volume akhir tabung adalah {volumeAkhir} cm2")


volumeAkhir = hitungVollumeTabungV2(t= tinggi, r= jariJari)
# jika parameter tidak mau urutan, bisa dengan cara seperti di atas


def hitungVollumeTabungV3(r: float, t: float = 15) -> float: # ada default value
    volume = (22/7) * (r** 2) * t
    return volume

volumeAkhir = hitungVollumeTabungV3(jariJari)
# karena tidak melempar value param tinggi
# maka nilai default t = 15 yang terpakai
import numpy
import math

# Soal bagian A
print("=== Program looping 1-100 ===")

for i in range(1, 101):
    print(i)

print(f"\n\n")
print("============================")

# Soal bagian B
print("=== Program mencetak variable ===")

x = int(input("Masukan nilai variable :"))

while x > 0:
    print(x)
    x -= 0.5

print(f"\n\n")
print("============================")

y = int(input("Masukan nilai variable :"))

for _ in range(int(y * 2)):
    print(y)
    y -= 0.5
    if y <= 0:
        break

print(f"\n\n")
print("==============================")
# Soal bagian C
print("=== Program akar kuadrat ===")

for i in range(1, 25):
    print(f"Akar kuadrat dari {i} adalah {math.sqrt(i)}")
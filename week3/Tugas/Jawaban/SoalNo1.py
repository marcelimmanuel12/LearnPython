# Soal no 1 bagian A
counter = 8
myList = []

for i in range(0, 9, 1):
    myList.append(f"List index ke {i} = {counter}")
    counter -=1

textoutput = f"\n".join(myList)
print(f"{textoutput}")

# Function join gunanya untuk menggabungkan isi data list menjadi 1 string yang ngambung
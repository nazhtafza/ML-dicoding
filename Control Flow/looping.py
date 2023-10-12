# looping menggunakna for
var_list = [1, 2, 3, 4, 5, 6]
for i in var_list:
    print(i)

for i in range(1, 6):  # -> apabila tidak menggunakan 1 yang merupakan start maka loop akan mulai dari 0
    print(i)

# for i in range(1, 3, 3):
#     print(i)

# While
counter = 1
while counter < 5:
    print(counter)
    counter += 1

# nested for loop
for i in range(1, 3):
    for j in range(1, 3):
        print(i, j)

# kontrol looping
# break -> menghentikan perulangan kemudian program otomatis keluar dari perulangan
for i in range(2):  # menjalankan looping pertama
    print("perulangan luar", i)
    for j in range(10):  # menjalankan looping kedua
        print("perulangan dalam", j)
        if j == 1:
            break  # berhenti jika j bernilai 1

# membuat class
class Mobil:
    # pass  # pass digunakan agar blok kode tidak menghasilkan error
    warna = "Merah"  # atribut dari kelas


# membuat object
print("== sebelum ==")
mobil1 = Mobil()
print(mobil1.warna)  # harus dipanggil dengan atribut

mobil2 = Mobil()
print(mobil2.warna)

# mengubah atribut
Mobil.warna = "hitam"  # mendefinisikan nama kelas.atribut

print("== setelah ==")
mobil1 = Mobil()
print(mobil1.warna)

mobil2 = Mobil()
print(mobil2.warna)

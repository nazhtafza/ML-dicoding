class Mobil:
    # __init__ -> fungsi khusus untuk menjadi constructor
    # self -> keyword yang sedang diproses saat ini
    def __init__(self) -> None:
        self.warna = "Merah"


mobil1 = Mobil()
mobil2 = Mobil()

print(mobil1.warna)
print(mobil2.warna)

# mengubah atribut instance
mobil1.warna = "Hitam"  # atribut dari mobil diubah menjadi warna hitam.

print(mobil1.warna)
print(mobil2.warna)  # atribut tetap merah

# menambahkan parameter lain dalam onstructor
print("== studi kasus motor ==")


class Motor:
    def __init__(self, nama, warna, kecepatan):
        self.nama = nama
        self.warna = warna
        self.kecepatan = kecepatan


# mendefinisikan parameter
motor1 = Motor("icikiwir", "hitam legam", 110)

# memanggil atribut
print(motor1.nama)
print(motor1.warna)
print(motor1.kecepatan)

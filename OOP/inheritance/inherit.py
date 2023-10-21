# INHERITANCE
print("== inheritance ==")

# mendeklarasikan kelas


class Kucing:
    def __init__(self, nama, ras, age) -> None:
        self.nama = nama
        self.ras = ras
        self.age = age

    def birthday(self):
        self.age += 1

# membuat kelas inherit


class Kucing_Rumah (Kucing):
    def umur(self):
        self.age += 1


# memanggil kelas biasa
kucing1 = Kucing("cemong", "himalaya", 9)
print(f"{kucing1.nama} dari ras {kucing1.ras} berumur {kucing1.age}")

kucing1.birthday()
print(f"jika cemong ultah maka ia berumur {kucing1.age} bulan")

# memanggil kelas inharitance
kucing2 = Kucing_Rumah("Pessy", "Jawir", 5)
print(f"{kucing2.nama} dari ras {kucing2.ras} berumur {kucing2.age}")

kucing2.umur()
print(f"jika dia ultah maka umurnya:{kucing2.age} ")

# SUPER
print("== super ==")

# membuat class sepeda


class Sepeda:
    def __init__(self, merek, warna, kecepatan) -> None:
        self.merek = merek
        self.warna = warna
        self.kecepatan = kecepatan

    def tambah_speed(self):
        self.kecepatan += 100

# membuat class inheritance


class RoadBike(Sepeda):
    def turbo(self):
        self.kecepatan += 150

    def tambah_speed(self):
        super().tambah_speed()
        print("kecepatan meningkat, wusss")


# kelas sepeda
sepeda1 = Sepeda("pligon", "jambon", 100)
print(
    f"sepeda merek {sepeda1.merek} berwarna {sepeda1.warna} mempunyai kecepatan {sepeda1.kecepatan}")

# menambah speed sepeda
sepeda1.tambah_speed()
print(f"speed bertambah ketika balapan sebesar {sepeda1.kecepatan}")

# kelas roadbike (sepeda)
sepeda2 = RoadBike("united", "hitam", 240)
print(
    f"road bike dengan merek {sepeda2.merek} berwarna {sepeda2.warna} punya kecepatan {sepeda2.kecepatan}")

sepeda2.turbo()
print(f"road bike speed bertambah ketika balapan sebesar {sepeda2.kecepatan}")

# METHOD
# mendeklarasikan fungsi
def my_decoration(func):
    # menambah fungsi wrapper untuk menambah perilaku sebelum dan setelah eksekusi dari fungsi func()
    def wrapper():
        print("sebelum fungsi dieksekusi")
        func()
        print("setelah fungsi dieksekusi")
    return wrapper

# membuat dekorator


@my_decoration
# def say_hello() memanggil dari fungsi func()
def say_hello():
    print("hallo dunia!")


# memanggil fungsi yang telah didekorasi
say_hello()

# OBJECT METHOD

# declare class Ultramen

print("== Ultraman Power Study Case ==")


class Ultramen:
    def __init__(self, nama, attack, defense) -> None:
        self.nama = nama
        self.attack = attack
        self.defense = defense

    # membuat object method
    def increase_attack(self):
        self.attack += 10


# mendefinisikan parameter
ultraman1 = Ultramen("Ultramen Tiga", 430, 450)
print(f"Ultraman 1 bernama: {ultraman1.nama}")
print(f"Kekuatan ultraman normal: {ultraman1.attack}")
print(f"Pertahanan ultraman normal: {ultraman1.defense}")

# mendefinisikan pertambahan attack
ultraman1.increase_attack()

# mencetak tambah attack
print(f"Pertambahan attack ultraman {ultraman1.attack}")

# Static Method
print("== Static Method ==")

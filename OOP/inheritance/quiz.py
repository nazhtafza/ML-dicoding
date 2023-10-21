# membuat class animal
class Animal:
    def __init__(self, name, age, species) -> None:
        self.name = name
        self.age = age
        self.species = species

# membuat class inherit


class Cat(Animal):
    def deskripsi(self):
        return f"{self.name} adalah kucing berjenis {self.species} yang sudah berumur {self.age} tahun"

    def suara(self):
        return "meow!"


# membuat instance class
myCat = Cat("Neko", 3, "Persian")
print(myCat.deskripsi())
print(myCat.suara())

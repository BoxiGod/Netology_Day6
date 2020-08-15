class Animal:
    fed = False
    collected = False
    animals = []

    def __init__(self, name="Vasya", weight=20):
        self.__class__.animals.append(self)
        self.name = name
        self.weight = weight # kg

    def feed(self):
        if not self.fed:
            self.fed = True

    def collect(self):
        if not self.collected:
            self.collected = True
            return True
        else:
            return False

    @classmethod
    def weight_sum(cls):
        weight_sum = 0
        for animal in cls.animals:
            weight_sum += animal.weight
        return weight_sum

    @classmethod
    def heaviest(cls):
        weight = 0
        name = ""
        for animal in cls.animals:
            if animal.weight > weight:
                weight = animal.weight
                name = animal.name
        return name

class Goose(Animal):
    voice = "Goo"

    def collect(self):
        if super().collect():
            return "Collected egg"

class Cow(Animal):
    voice = "Moo"

    def collect(self):
        if super().collect():
            return "Collected milk"

class Sheep(Animal):
    voice = "Shee"

    def collect(self):
        if super().collect():
            return "Collected wool"

class Chicken(Animal):
    voice = "Chick"

    def collect(self):
        if super().collect():
            return "Collected egg"

class Goat(Animal):
    voice = "Goa"

    def collect(self):
        if super().collect():
            return "Collected milk"

class Duck(Animal):
    voice = "Krya"

    def collect(self):
        if super().collect():
            return "Collected egg"

grey = Goose("Grey", 40)
white = Goose("White", 37)
cow = Cow("Manka", 800)
barashek = Sheep("Barashek", 100)
kudryavi = Sheep("Kudryavi", 98)
ko_ko = Chicken("Ko-ko", 20)
kukareku = Chicken("Kukareku", 21)
roga = Goat("Roga", 70)
kopita = Goat("Kopita", 75)
kryakva = Duck("Kryakva", 50)
print(kopita.collect())
print(Animal.weight_sum())
print(Animal.heaviest())
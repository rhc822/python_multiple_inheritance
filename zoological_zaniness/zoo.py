from animals import Penguin
from habitats import Habitat

Bob = Penguin("Bob")
print(Bob)
Bob.run()
Bob.swim()

Zippy = PaintedDog("Zippy")
print(Zippy)

seaworld = Habitat("Sea World")
seaworld.add_animal(Bob)
print(seaworld)



for animal in seaworld.animals:
    print(animal)
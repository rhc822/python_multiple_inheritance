from animals import PaintedDog
from animals import Penguin
from habitats import Habitat
from habitats import Aquarium

Bob = Penguin("Bob")
# print(Bob)
# Bob.run()
# Bob.swim()

Ralph = PaintedDog("Ralph")
# print(Ralph)

seaworld = Aquarium("Sea World")
seaworld.add_swimmer_pythonic(Bob)
seaworld.add_swimmer_pythonic(Ralph)
seaworld.add_swimmer_type_check(Ralph)


for animal in seaworld.animals:
    print(animal)
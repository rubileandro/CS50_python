import random


class Hat:
    # class varaible
    houses = ["Gryffindor", "Hufflepuff", "Ravenclasw", "Slytherin"]
    
    @classmethod
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))


Hat.sort("Harry")
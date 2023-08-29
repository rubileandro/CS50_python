class Student:
    def __init__ (self, name, house):
        # Validating
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        # Assigning
        self.name = name
        self.house = house


    def __str__(self):
        return f"{self.name} from {self.house}"
    
    # Getter
    def house(self):
        return self.house
    
    # Setter
    def house(self, house):
        self.house = house

def main():
    student = get_student()
    print(student)

def get_student():
    name = input("Name: ")
    house = input("House: ")
    # Constructor call
    return Student(name, house)




if __name__ == "__main__":
    main()

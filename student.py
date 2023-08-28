class Student:
    def __init__ (self, name, house):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

def main():
    student = get_student()
    print(student)
# # Alternative
# def get_name():
#     # Immediately returning the return value of input func call
#     return input("Name: ")

# def get_house():
#     return input("Name: ")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    # Constructor call
    return Student(name, house)




if __name__ == "__main__":
    main()

def main():
    student = get_student()
    if student["name"] == "Padma":
        student["house"] = "Ravenclaw"
    print(f"{student['name']} from {student['house']}")

# # Alternative
# def get_name():
#     # Immediately returning the return value of input func call
#     return input("Name: ")

# def get_house():
#     return input("Name: ")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return {"name": name, "house": house}


if __name__ == "__main__":
    main()

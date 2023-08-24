def main():
    student = get_student()
    print(f"{student[0]} from {student[1]}")

# # Alternative
# def get_name():
#     # Immediately returning the return value of input func call
#     return input("Name: ")

# def get_house():
#     return input("Name: ")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return (name, house)


if __name__ == "__main__":
    main()

with open("students.csv") as file:
    for line in file:
        # create and assign in parallel
        name, house = line.rstrip().split(",")
        print(f"{name} is in {house}")

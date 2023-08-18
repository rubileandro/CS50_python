names = []

with open("names.txt") as file:
    for line in file:
        # appending to the list in memory not the file
        names.append(line.rstrip())


for name in sorted(names):
    print(f"Hello, {name}")

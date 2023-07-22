# Option 1
# # What is your name?
# name = input("What's your name? ")

# # Remove whitespace & capitalize name
# name = name.strip().title()

# # Greet user
# #print("Hello,", name, sep="???")
# print(f"Hello, {name}")

# Option 2
# get name, remove whitepsace and capitalize
name = input("What's your name?").strip().title()

# Split name
first, name = name.split(" ")

# Greet user
#print("Hello,", name, sep="???")
print(f"Hello, {first}")


# # overide default value \n
# print("Hello,", end="")
# print(name)
x = int(input("What's x?"))
y = int(input("what's y?"))

# # # Version 1
# if x < y:
#     print("x is less than y.")
# if x > y:
#     print("x is greater than y.")
# if x == y:
#     print("x is equal to y.")

# # Version 2 mutually exclusive conditions
# if x < y:
#     print("x is less than y.")
# elif x > y:
#     print("x is greater than y.")
# elif x == y:
#     print("x is equal to y.")

# # Version 3
# if x < y:
#     print("x is less than y.")
# elif x > y:
#     print("x is greater than y.")
# else:
#     print("x is equal to y.")

# # Version 4
# if x < y or x > y:
#     print("x is not equal to y")
# else:
#     print("x is equal to y")

# Version 5
if x != y:
    print("x is not equal to y")
else:
    print("x is equal to y")

# # Modulo

#Version 1
# x = int(input("What's x? "))

# if x % 2 == 0:
#     print("Even.")
# else:
#     print("Odd.")

# # Version 2
def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")


# Version 2.0
# def is_even(n):
#     if n % 2 == 0:
#         return True
#     else:
#         return False

# # Version 2.1 Pythonic    
# def is_even(n):
#     return True if n % 2 == 0 else False

#version 2.2
def is_even(n):
    return n % 2 == 0


main()

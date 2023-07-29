# # Version 1
# x = float(input("What's x? "))
# y = float(input("What's y? "))

# z = round(x + y)

# print(f"{z:,}")

# # Version 2
# x = float(input("What's x? "))
# y = float(input("What's y? "))

# z = round(x / y, 2)

# print(z)

# # Version 3 f-string
# x = float(input("What's x? "))
# y = float(input("What's y? "))

# z = x / y

# print(f"{z:.2f}")

# Version 4 with return
def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))

def square(n):
    # return n * n
    # return pow(n, 2)
    return n ** 2

main()

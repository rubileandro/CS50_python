import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

# Iterate over every name at the prompt
for arg in sys.argv[1:]:
    print("hello, my name is", arg)

import cowsay
import sys

# Proactive error checking
if len(sys.argv) == 2:
    # Cow
    cowsay.cow("hello," + sys.argv[1])
    # # T-rex
    # cowsay.trex("hello," + sys.argv[1])

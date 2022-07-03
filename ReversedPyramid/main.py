# Messages
def print_star():
    print("*", end = "")


def print_space():
    print(" ", end = "")


def print_new_line():
    print('')


# Variables
rows = int(input('Enter number of rows: ')) + 1
cols = int(rows)

# Loops
for r in range(rows):

    for s in range(rows-cols):
        print_space()

    cols -= 1

    for c in range(cols):
        print_star()
        print_space()

    print_new_line()


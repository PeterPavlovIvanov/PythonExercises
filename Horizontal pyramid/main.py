# Constants
WELCOME_MESSAGE = "Enter a number: "
MINUS_ONE = -1
ZERO = 0
ONE = 1
TWO = 2


# Messages
def print_new_line(i):
    if i != ONE:
        print("")


def print_number(num):
    print(f"{num} ", end = "")


# User input
input_number = int(input(WELCOME_MESSAGE))


# Loops
for i in range(ONE, input_number + TWO):
    for j in range(ONE, i):
        print_number(j)
        j += ONE
    print_new_line(i)
    i += ONE


for i in range(input_number, ZERO, MINUS_ONE):
    for j in range(ONE, i):
        print_number(j)
        j += ONE
    print_new_line(i)
    i += ONE

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# Constants
TEN = int(10)
FUNCTION = "f(n) = n + nn + nnn"
WELCOME_MESSAGE = "Enter a number: "


# Messages
def print_equation(number):
    result_tuple = calculate_numbers(number)
    print(f'{result_tuple[0]} + {result_tuple[1]} + {result_tuple[2]} = {result_tuple[3]}')


# Logic
def calculate_numbers(n):
    nn = int(n * TEN) + n
    nnn = int(nn * TEN) + n
    result = int(n + nn + nnn)
    result_tuple = (n, nn, nnn, result)
    return result_tuple


# User Input
print(FUNCTION)
input_number = int(input(WELCOME_MESSAGE))
print_equation(input_number)

# Messages
def print_list(data):
    print(f'List, {data}')


def print_tuple(data):
    print(f'Tuple, {data}')


# User input
userInput = input("Enter numbers separated with commas: ")


# List
userList = userInput.split(sep = ',')
print_list(userList)


# Tuple
userTuple = tuple(userInput.split(sep =','))
print_tuple(userTuple)


import math

# is strobogrammatic odd number
def is_odd_strobogrammatic(num_as_text):
    result = 0
    mid_index = int(len(num_as_text) / 2)
    mid = num_as_text[mid_index]
    if not ((mid == '0') | (mid == '1') | (mid == '8')):
        result = 0
        return result

    first_half = num_as_text[0:mid_index]
    second_half = num_as_text[mid_index + 1:int(len(num_as_text) + 1)]
    second_half = second_half[::-1]  # reverse

    for i in range(0, int(len(first_half))):
        is_same_number = first_half[i] == second_half[i]
        is_0_1_8 = (first_half[i] == '0') | (first_half[i] == '1') | (first_half[i] == '8')
        is_6_to_9 = (first_half[i] == '6') & (second_half[i] == '9')
        is_9_to_6 = (first_half[i] == '9') & (second_half[i] == '6')

        if (is_same_number & is_0_1_8) | is_6_to_9 | is_9_to_6:
            result = 1
        else:
            result = 0
            return result

    return result


# is strobogrammatic even number
def is_even_strobogrammatic(num_as_text):
    first_half = num_as_text[0:int(len(num_as_text) / 2)]
    second_half = num_as_text[int(len(num_as_text) / 2):int(len(num_as_text) + 1)]
    second_half = second_half[::-1]  # reverse
    result = 1

    for i in range(0, int(len(first_half))):
        is_same_number = first_half[i] == second_half[i]
        is_0_1_8 = (first_half[i] == '0') | (first_half[i] == '1') | (first_half[i] == '8')
        is_6_to_9 = (first_half[i] == '6') & (second_half[i] == '9')
        is_9_to_6 = (first_half[i] == '9') & (second_half[i] == '6')

        if (is_same_number & is_0_1_8) | is_6_to_9 | is_9_to_6:
            result = 1
        else:
            result = 0
            return result

    return result


# is Strobogrammatic odd or even it must contain only the numbers 0, 1, 8, 6, 9
def is_strobogrammatic(num_as_text):
    for letter in num_as_text:
        if (letter != '0') & (letter != '1') & (letter != '8') & (letter != '6') & (letter != '9'):
            return 0

    if len(num_as_text) % 2 == 1:
        return is_odd_strobogrammatic(num_as_text)
    else:
        return is_even_strobogrammatic(num_as_text)


# main starts here
num = input("Enter a number: ")
start_number = math.pow(10, int(num) - 1)
end_number = math.pow(10, int(num))

for i in range(int(start_number), int(end_number)):
    if is_strobogrammatic(str(i)):
        print(i)


def is_text_a_palindrome(num_text):
    is_odd = len(num_text) % 2 != 0
    adjust = int(0)
    if is_odd:
        adjust += 1

    f_half = num_text[0:int(len(num_text) / 2)]
    s_half = num_text[int(len(num_text) / 2) + adjust:int(len(num_text) / 2) + 1]
    s_half = s_half[::-1]

    if f_half == s_half:
        return 1
    else:
        return 0


# Enter a number, reverse it add the reversed to the original, repeat until the sum is palindrome
num = int(input("Enter a number: "))
count_max = 99
is_palindrome = 0
not_found = 0
while (is_palindrome != 1) & (not_found != 1):
    num_text = str(num)
    num_text = num_text[::-1]
    print(f'{num} + {num_text} = {num + int(num_text)}')
    num += int(num_text)  # python removes zeros automatically
    num_text = str(num)

    if count_max == 0:
        not_found = 1
    elif is_text_a_palindrome(num_text):
        is_palindrome = 1
    count_max -= 1

if is_palindrome == 1:
    print(f'Found Palindrome: {num}')
else:
    print(f'Could not find palindrome in 99 tries :(')
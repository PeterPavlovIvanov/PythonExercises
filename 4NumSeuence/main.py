
num = int(input("Find the Nth number from the sequence where each number is the sum of the previous 4: "))
current = 1
prev_1 = 1
prev_2 = 1
prev_3 = 1
prev_4 = 1

for i in range (1, num + 1):
    if i <= 4:
        continue
    else:
        current = prev_1 + prev_2 + prev_3 + prev_4
        prev_4 = prev_3
        prev_3 = prev_2
        prev_2 = prev_1
        prev_1 = current

print(f'{num}th number from the sequence is: {current}')
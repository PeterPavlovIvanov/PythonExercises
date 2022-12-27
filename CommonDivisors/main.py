num_1 = int(input("Enter the first number: "))
num_2 = int(input("Enter the second number: "))
bigger_num = max(num_1, num_2)
result = []
for i in range(1, bigger_num + 1):
    if(num_1 % i == 0) & (num_2 % i == 0):
        result.append(i)

print(f'Common divisors for both numbers are: {result}')

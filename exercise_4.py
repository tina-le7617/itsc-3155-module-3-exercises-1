sum = 0
i = 0
while (i < 5):
    try:
        user_input = int(input(f'Enter int #{i + 1}: '))
        sum += user_input
        i += 1
    except ValueError:
        print("Invalid input. Please enter an int")

print(f'Your sum is {sum}')

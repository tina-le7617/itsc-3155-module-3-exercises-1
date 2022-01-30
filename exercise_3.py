def dict_count(letters):
    count = {}

    for char in letters.lower().replace(" ", ""):
        if char in count:
            count[char] += 1
        else:
            count[char] = 1

    return count

user_input = input("Enter a string: ")
count = dict_count(user_input)
print (count)
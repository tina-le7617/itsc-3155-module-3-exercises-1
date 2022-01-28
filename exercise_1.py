def get_unique_list(numbers):
    list_set = set(numbers)
    unique_list = (list(list_set))
    return unique_list 

my_list = [1, 2, 3, 2, 1, 4, 4, 4, 1, 1, 10, 2, 3, 5]
unique_list = get_unique_list(my_list)
print(unique_list)
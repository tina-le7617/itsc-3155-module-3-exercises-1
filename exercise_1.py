'''''
https://www.geeksforgeeks.org/python-get-unique-values-list/
'''''

def get_unique_list(num):
    # Taking a list passed in from the parameters, create a set with those numbers
    set_num = set(num)

    # Create list using list() method that will convert the set back into a list
    unique_list = (list(set_num))
    return unique_list 

my_list = [1, 2, 3, 2, 1, 4, 4, 4, 1, 1, 10, 2, 3, 5]
unique_list = get_unique_list(my_list)
print(unique_list)
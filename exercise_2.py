'''''
https://www.geeksforgeeks.org/python-combine-two-dictionary-adding-values-for-common-keys/

'''''

def get_combined_dict(dict_1, dict_2):
    # Create a new, empty dictionary
    combined_dict = {}

    # Loop through first dictionary
    for key in dict_1:

        # If the key is in either dictionaries > Add values & store into new dictionary
        if key in dict_1 and dict_2:
            combined_dict[key] = dict_2[key] + dict_1[key]
        else:
            pass
    
    return combined_dict

my_dict_1 = {'a': 5, 'b': 12, 'c': 3, 'd': 9, 'd': 10}
my_dict_2 = {'b': 4, 'c': 9, 'd': 10, 'e': 16, 'f': 1, 'd': 2}

combined_dict = get_combined_dict(my_dict_1, my_dict_2)
print(combined_dict)
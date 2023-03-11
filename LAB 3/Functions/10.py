def unique_elem(input_list):
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

a = [1, 2, 2, 3, 3, 4, 4, 5, 6, 7, 8, 8, 8, 9, 9, 10]
print(unique_elem(a))


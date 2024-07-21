def get_even_squares(lst):
    return [y**2 for y in lst if y % 2 == 0]
########################################

def slice_list(lst, start, end):
    return lst[start:end]

##########################################
def parse_input_list(input_str):
    input_str = input_str.strip()[1:-1]  
    return list(map(int, input_str.split(',')))

#####################################
input_str = input("Enter the list of integers: ")
input_list = parse_input_list(input_str)

##################################
even_squares_list = get_even_squares(input_list)
print(f"List of squares of even numbers: {even_squares_list}")

####################################
input_str = input("Re-enter the list of integers: ")
input_list = parse_input_list(input_str)

##################################
start_index = int(input("Enter start index: "))
end_index = int(input("Enter end index: "))



##################################
sliced_list = slice_list(input_list, start_index, end_index)
print(f"Sublist: {sliced_list}")

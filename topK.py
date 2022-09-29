from curses.ascii import isdigit
import re
import itertools

def bag_to_set(old_list):
    new_list = []
    if old_list == []:
        new_list = []
    else:
        if (old_list[0] not in old_list[1:]):
            new_list = [old_list[0]] + bag_to_set(old_list[1:])
        else:
            new_list = bag_to_set(old_list[1:])
    return new_list 


# defining a function to find the frequencies for every unique element in the list recursively
def frequencies(listA):
	
	# checking the base condition when the list is empty
	if len(listA) == 0:
		# returning an empty dictionary
		return {}

	# processing the value of other elements of list except the first element
	# so we need to call the recursive function exclusing the first element
	freq = frequencies(listA[1:])
	
	# processing the first element of the list
	# checking if the first element is already present in the freq dictionary or not
	if listA[0] in freq:
		# if present increment its count
		freq[listA[0]] += 1
	# if not present store it into the dictionary
	# as it is found for the first time make its value as 1
	else:
		freq[listA[0]] = 1

	# return the frequencies dict formed
	return freq




if __name__ == "__main__":
    s = []
    st = []
    arrInt = []
    arrFloat = []

    with open('Documents/cosc_4315/input.txt') as file:
        lines = file.readlines() 

    org_float = list(map(lambda i: re.findall('-?\d+\.{1}\d+', i), lines))
    org_int = list(map(lambda i: re.findall(r'-?\b(?<!\.)\d+(?!\.)\b', i), lines))
    flatten=lambda i: sum(map(flatten,i),[]) if isinstance(i,list) else [i]


    float_list = flatten(org_float)
    int_list = flatten(org_int)

    f_nums = list(map(float, float_list))
    i_nums = list(map(int, int_list))

    fl_sorted = sorted(f_nums)
    int_sorted = sorted(int_list)

    unique_floats = bag_to_set(fl_sorted)
    unique_ints = bag_to_set(int_sorted)



    
    print(float_list)
    print(f_nums)
    print(fl_sorted)
    print(unique_floats, '\n\n')    
    print('===================================================================================================')
    print(int_list)
    print(i_nums)
    print(int_sorted)
    print(unique_ints)

    

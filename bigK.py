from curses.ascii import isdigit
from itertools import groupby
import re
import itertools








def recursive_sort(a_list):
    def helper_function(list_to_be_sorted, list_already_sorted):
        new = []
        if len(list_to_be_sorted) == 0:
            return list_already_sorted
        else:    
            x = min(list_to_be_sorted)    
            list_to_be_sorted.remove(x)
            new.append(x)
            return helper_function(list_to_be_sorted, list_already_sorted + new)
    return helper_function(a_list, [])





def rtraverse(seq, i=0):
    if i < len(seq):
        print(seq[i])
        rtraverse(seq, i+1)


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


def frequencies(lst):
    if len(lst) == 0:
        return []
    else:
        return [lst.count(lst[0])] + frequencies(lst[lst.count(lst[0]):])


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
    int_sorted = sorted(i_nums)
    
    print(f_nums)
    print(fl_sorted)



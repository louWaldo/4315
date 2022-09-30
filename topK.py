from curses.ascii import isdigit
from itertools import groupby
import re
import itertools

from numpy import FPE_DIVIDEBYZERO



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




def rtraverse2(seq, j, t):
    if j < len(seq):
        if seq[j][1] == t:
            print(seq[j])
        rtraverse2(seq, j+1, t)



def rtraverse(seq, k, i):
    if i < k:
        print (seq[i])
        rtraverse(seq, k, i+1)
    if i == k:
        j = 0
        temp = seq[k:]
        t = seq[i][1]
        print('+++++++++++++++++++++++')
        rtraverse2(temp, j, t)
        





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

    orgFloat = list(map(lambda i: re.findall('-?\d+\.{1}\d+', i), lines))
    orgInt = list(map(lambda i: re.findall(r'-?\b(?<!\.)\d+(?!\.)\b', i), lines))
    flatten=lambda i: sum(map(flatten,i),[]) if isinstance(i,list) else [i]


    floatFlat = flatten(orgFloat)
    intFlat = flatten(orgInt)

    floatNums = list(map(float, floatFlat))
    intNums = list(map(int, intFlat))

    floatSorted = sorted(floatNums)
    intSorted = sorted(intNums)

    floatUnique = bag_to_set(floatSorted)
    intUnique = bag_to_set(intSorted)


    intFreq = frequencies(intSorted)
    fpFreq = frequencies(floatSorted)

    intZip = zip(intUnique, intFreq)
    fpZip = zip(floatUnique, fpFreq)

    fpList = list(fpZip)
    intList = list(intZip)

    intLast = sorted(intList, key = lambda x: x[1], reverse=True)
    fpLast = sorted(fpList, key = lambda x: x[1], reverse=True)

    # print(orgInt, '\n')
    # print(intFlat)
    # print(intNums)
    # print(intSorted)
    # print(intUnique)
    # print(intFreq)
    # print(intList)
    # print(intLast)
    k = 3
    i = 0
    rtraverse(intLast, k, i)


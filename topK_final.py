from curses.ascii import isdigit
from itertools import groupby
import re
import itertools
import sys

def convTup(tup):
    st = ''.join(map(str,tup))
    lastchr = len(st)-2
    ot = st[1:lastchr]
    fot = ot.replace(',','')
    return (fot + '\n')

def writeOut(strO,out):
    with open(out,"a") as f:
        f.write(convTup((str(strO) + '\n' )))    
        f.close()
    return 0

def writeTout(strT,out):
    with open(out,"a") as f:
        f.write(strT)
    f.close()
    return 0

def freqNum(k,infile,out):
    with open(infile) as file:
         lines = file.readlines()

    orgFloat = list(map(lambda i: re.findall('-?\d+\.{1}\d+', i), lines))
    orgInt = list(map(lambda i: re.findall(r'-?\b(?<!\.)\d+(?!\.)\b', i), lines))
    flatten=lambda i: sum(map(flatten,i),[]) if isinstance(i,list) else [i]
    flatten=lambda i: sum(map(flatten,i),[]) if isinstance(i,list) else [i]
    strToInt = lambda i: list(map(int, i))
    strToFloat = lambda i: list(map(float, i))
    unique = lambda i: bag_to_set(i)
    freq = lambda i: frequencies(i)
    ziptie = lambda i, j: zip(i, j)
    sortByFreq = lambda i: sorted(i, key = lambda j: j[1], reverse = True)

    intFlat = flatten(orgInt)
    floatFlat = flatten(orgFloat)

    intNums = strToInt(intFlat)
    floatNums = strToFloat(floatFlat)

    floatSorted = sorted(floatNums)
    intSorted = sorted(intNums)

    floatUnique = unique(floatSorted)
    intUnique = unique(intSorted)

    intFreq = freq(intSorted)
    fpFreq = freq(floatSorted)

    intZip = ziptie(intUnique, intFreq)
    fpZip = ziptie(floatUnique, fpFreq)
    
    fpList = list(fpZip)
    intList = list(intZip)

    intLast = sortByFreq(intList)
    fpLast = sortByFreq(fpList)

    file.close()
    i = 0
    rtraverse(intLast, k, out, i)
    rtraverse(fpLast, k, out, i)

def rtraverse2(seq, j, out, t):
    if j < len(seq):
        if seq[j][1] == t:
            print(seq[j])
            writeOut(seq[j],out)
        rtraverse2(seq, j+1, out, t)

def rtraverse(seq, k, out, i):
    if i < k:
        if type(seq[i][0]) == int and i == 0:
            writeTout("integer:"+'\n',out)
        elif type(seq[i][0]) == float and i == 0:
            writeTout("real:"+'\n',out)
        writeOut(seq[i],out)
        rtraverse(seq, k, out, i+1)
    if i == k:
        j = 0
        temp = seq[k:]
        t = seq[i][1]
        rtraverse2(temp, j, out, t)
        
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
    argl = sys.argv[1].split(';') 
    i = 0

    for pattern in argl:
        if i == 0:
            k = "".join([val for val in pattern[(pattern.find("=")+1):]])
        elif i == 1:
            infile = "".join([val for val in pattern[(pattern.find("=")+1):]])
        else:
            out = "".join([val for val in pattern[(pattern.find("=")+1):]])
        i+=1
    freqNum(int(k),infile,out)
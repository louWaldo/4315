from curses.ascii import isdigit
import re

def frequencies(arr, n, k):
    mp = {}
    for i in range(n):
        if(arr[i] in mp):
            mp[arr[i]] += 1
        else:
            mp[arr[i]] = 1

    a = [0]*(len(mp))
    j = 0
    for i in mp:
        a[j] = [i, mp[i]]
        j += 1
    
    for i in range(len(a)):
        print(a[i][0], "  ", a[i][1])

    a = sorted(a, key = lambda x: x[0], reverse = True)
    a = sorted(a, key = lambda x: x[1], reverse = True)

    #display top k
    print(k, "numbers with most occurences are: ")
    for i in range(k):
        print(a[i][0], "  ", a[i][1])
    


if __name__ == "__main__":
    s = []
    st = []
    arrInt = []
    arrFloat = []

    with open('computer/hello/COSC_4315/input.txt') as file:
        lines = file.readlines() 


    for i in lines:
        s.append(re.findall(r'[.\d]+', i))

    st = filter(lambda i: re.split(r'[.\d]+', i), lines)
    
    print(*s)
    print('fuck you')
    print(*st)

    #for k in s:
    #    for j in s[k]:
     #       if j.isnumeric():
      #          arrInt.append(int(j))
       #     else:
        #        arrFloat.append(float(j))
        




    #file = open('computer/hello/COSC_4315/input.txt')
    #contents = file.read()
    #myList = contents.split()

    #arrInt = []
    #arrFloat = []
    #for i in myList:
    #    if(i.isdigit()):
    #        arrInt.append(int(i))
    #    else:
    #        arrFloat.append(float(i))

    #n = len(arrInt)
    #m = len(arrFloat)

    #k = int(input())

    #print('Int Frequencies: ')
    #frequencies(arrInt, n, k)

    #print('Float Frequencies: ')
    #frequencies(arrFloat, m, k)
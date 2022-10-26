def merge(a, b):
    if len(a) == 0:
        return b
    elif len(b) == 0:
        return a
    elif a[0] < b[0]:
        return [a[0]] + merge(a[1:], b)
    else:
        return [b[0]] + merge(a, b[1:])

def mergesort(x):
    if len(x) < 2:
        return x
    else:
        h = len(x) // 2
        return merge(mergesort(x[:h]), mergesort(x[h:]))


 
def insertionSort(arr):
     list1 = []
     for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key
 


def inSort(sorted, list):
    if(len(list)==0):
        return sorted
    elif(len(sorted)==0):
        return inSort(list[0], list[1:])
    x = list[0]
    sorted = filter(lambda a: a<=x, sorted) + x + filter()
 


def sum(l):
 if(len(l) == 1):
   return l[0]
 else:
   return l.pop() + sum(l)



x = [1, 2, 3, 4, 5]
y = sum(x)
print(y)










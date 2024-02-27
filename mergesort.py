import random

def mergeSort(array, start, end):
    if end - start + 1 <= 1:
        return array
    
    middle = (start + end) // 2

    mergeSort(array, start, middle)
    mergeSort(array, middle + 1, end)

    merge(array, start, middle, end)

    return array

def merge(array, start, middle, end):
    temp1 = array[start: middle + 1]
    temp2 = array[middle + 1: end + 1]

    i = 0
    j = 0 
    k = start 

    while i < len(temp1) and j < len(temp2):
        if temp1[i] <= temp2[j]:
            array[k] = temp1[i]
            i += 1
        else:
            array[k] = temp2[j]
            j += 1
        k += 1

    while i < len(temp1):
        array[k] = temp1[i]
        i += 1
        k += 1
    while j < len(temp2):
        array[k] = temp2[j]
        j += 1
        k += 1



arr = list(range(20))
random.shuffle(arr)
arr = mergeSort(arr, 0, 19)
print(arr)
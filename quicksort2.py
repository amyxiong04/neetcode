def partition(arr, start, end):
    pivot = arr[start]

    while start < end:
        while start < end and arr[end] >= pivot:
            end -= 1
        arr[start] = arr[end]
        while start < end and arr[start] <= pivot:
            start += 1
        arr[end] = arr[start]
    arr[start] = pivot
    return start

def quicksort(array, start, end):
    if start < end:
        part = partition(array, start, end)
        quicksort(array, start, part - 1)
        quicksort(array, part + 1, end)


array = [9,6,4,2,8,7,4]
quicksort(array, 0, 6)
print(array)
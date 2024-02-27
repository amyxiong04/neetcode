def bucketsort(array):
    counts = [0, 0, 0, 0]
            # 0  1  2  3

    for i in array:
        counts[i] += 1
    
    n = 0
    for i in range(len(counts)):
        for j in range(counts[i]):
            array[n] = i
            n += 1 
    return array

array = [2, 1, 3, 2, 1, 3, 0]
sorted = bucketsort(array)
print(sorted)

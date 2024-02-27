import random
def insertionSort(array):
    for i in range (1, len(array)):
        j = i - 1
        while j >= 0 and array[j + 1] < array[j]:
            temp = array[j + 1]
            array[j + 1] = array[j]
            array[j] = temp
            j = j - 1
        
    return array


def insert_sort(nums):
    for tb in range(1, len(nums)):
        move = nums[tb]
        hand = tb - 1
        while hand >= 0 and nums[hand] > move:
            nums[hand+1] = nums[hand]
            hand -= 1
        nums[hand+1] = move
    return nums


arr = [5, 4, 3, 2, 1]
arr1 = list(range(20))
random.shuffle(arr1)

print(arr1)
insert_sort(arr1)
print(arr1)


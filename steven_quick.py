

def partition(nums, left, right):
    tmp = nums[left]
    while left < right:
        while nums[right] >= tmp:
            right -= 1
        nums[left] = nums[right]
        while nums[left] <= tmp:
            left += 1
        nums[right] = nums[left]
    nums[left] = tmp
    return left

def quick(nums, left, right):
    if left < right:
        mid = partition(nums, left, right)
        quick(nums, left, mid-1)
        quick(nums, mid+1, right)


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(nums)
quick(nums, 0, 9)     
print(nums)  
    
